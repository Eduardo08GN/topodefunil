#!/usr/bin/env python3
"""Download a video via yt-dlp, or resolve a local file path.

Also fetches subtitles (manual first, then auto-generated) in VTT format so
transcribe.py can parse them without needing Whisper.

Login-walled sources (Facebook / Instagram reels) authenticate via cookies:
- WATCH_COOKIES_FILE: path to a Netscape cookies.txt. Safe to always include —
  yt-dlp scopes cookies by domain, so FB cookies never leak to other hosts —
  and it works with the browser open (unlike the browser cookie DB).
- WATCH_COOKIES_BROWSER: a browser name for --cookies-from-browser (e.g.
  "chrome"). Applied only as a retry when the anonymous attempt produced no
  file, because the browser cookie DB is locked while that browser is open, so
  it must stay a rescue path (see RUNBOOK-watch-videos.md, gotcha #2).
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


VIDEO_EXTS = {".mp4", ".mkv", ".webm", ".mov", ".m4v", ".avi", ".flv", ".wmv"}


def _ytdlp_base() -> list[str]:
    """yt-dlp invocation prefix.

    Prefer pip's `yt_dlp` module (always updatable with `pip install -U yt-dlp`)
    over a possibly-stale `yt-dlp.exe` on PATH (e.g. the one in System32 that
    breaks the Facebook extractor — RUNBOOK-watch-videos.md, gotcha #1).
    """
    try:
        import yt_dlp  # noqa: F401
        return [sys.executable, "-m", "yt_dlp"]
    except Exception:
        exe = shutil.which("yt-dlp")
        if exe:
            return [exe]
        raise SystemExit("yt-dlp is not installed. Install with: pip install -U yt-dlp")


def _cookie_file_args() -> list[str]:
    """--cookies from WATCH_COOKIES_FILE, if set and present. Always safe."""
    f = os.environ.get("WATCH_COOKIES_FILE", "").strip()
    if f:
        p = Path(f).expanduser()
        if p.exists():
            return ["--cookies", str(p)]
        print(f"[watch] WATCH_COOKIES_FILE set but not found: {p}", file=sys.stderr)
    return []


def _cookie_browser_args() -> list[str]:
    """--cookies-from-browser from WATCH_COOKIES_BROWSER. Rescue-only (see module docstring)."""
    b = os.environ.get("WATCH_COOKIES_BROWSER", "").strip()
    return ["--cookies-from-browser", b] if b else []


def is_url(source: str) -> bool:
    if source.startswith("-"):
        return False
    parsed = urlparse(source)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def resolve_local(path: str) -> dict:
    p = Path(path).expanduser().resolve()
    if not p.exists():
        raise SystemExit(f"File not found: {p}")
    if p.suffix.lower() not in VIDEO_EXTS:
        print(
            f"[watch] warning: {p.suffix} is not a known video extension, proceeding anyway",
            file=sys.stderr,
        )
    return {
        "video_path": str(p),
        "subtitle_path": None,
        "info": {"title": p.name, "url": str(p)},
        "downloaded": False,
    }


def _pick_subtitle(out_dir: Path) -> Path | None:
    candidates = sorted(out_dir.glob("video*.vtt"))
    if not candidates:
        return None
    preferred = [
        c for c in candidates
        if any(marker in c.name for marker in (".en.", ".en-US.", ".en-GB.", ".en-orig."))
    ]
    return preferred[0] if preferred else candidates[0]


def _pick_video(out_dir: Path) -> Path | None:
    for ext in (".mp4", ".mkv", ".webm", ".mov", ".m4a", ".mp3", ".opus"):
        for candidate in out_dir.glob(f"video*{ext}"):
            return candidate
    for candidate in out_dir.glob("video.*"):
        if candidate.suffix.lower() in VIDEO_EXTS:
            return candidate
    return None


def fetch_captions(url: str, out_dir: Path) -> dict:
    """Fetch metadata and best available VTT captions without downloading video."""
    out_dir.mkdir(parents=True, exist_ok=True)
    output_template = str(out_dir / "video.%(ext)s")
    cmd = _ytdlp_base() + [
        "--skip-download",
        "--write-info-json",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs", "en.*",
        "--sub-format", "vtt",
        "--convert-subs", "vtt",
        "--no-playlist",
        "--ignore-errors",
    ] + _cookie_file_args() + [
        "-o", output_template,
        "--",
        url,
    ]
    subprocess.run(cmd, stdout=sys.stderr, stderr=sys.stderr)
    subtitle = _pick_subtitle(out_dir)
    info = _read_info(out_dir / "video.info.json", url)
    return {
        "video_path": None,
        "subtitle_path": str(subtitle) if subtitle else None,
        "info": info or {"url": url},
        "downloaded": False,
    }


def _read_info(info_path: Path, url: str) -> dict:
    info: dict = {}
    if info_path.exists():
        try:
            raw = json.loads(info_path.read_text(encoding="utf-8"))
            info = {
                "title": raw.get("title"),
                "uploader": raw.get("uploader") or raw.get("channel"),
                "duration": raw.get("duration"),
                "url": raw.get("webpage_url") or url,
            }
        except Exception as exc:
            print(f"[watch] info.json parse failed: {exc}", file=sys.stderr)
            info = {"url": url}
    return info


def download_url(
    url: str,
    out_dir: Path,
    audio_only: bool = False,
) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    output_template = str(out_dir / "video.%(ext)s")

    fmt = "ba/bestaudio" if audio_only else "bv*[height<=720]+ba/b[height<=720]/bv+ba/b"
    base = _ytdlp_base()
    common = [
        "-N", "8",
        "-f", fmt,
        "--merge-output-format", "mp4",
        "--write-info-json",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs", "en.*",
        "--sub-format", "vtt",
        "--convert-subs", "vtt",
        "--no-playlist",
        "--ignore-errors",
    ]

    def run(extra: list[str]) -> subprocess.CompletedProcess:
        # yt-dlp may exit non-zero if a subtitle variant fails (e.g. 429) even
        # when the video itself downloaded fine. Treat "video file present" as
        # success (checked by the caller via _pick_video).
        return subprocess.run(
            base + common + extra + ["-o", output_template, "--", url],
            stdout=sys.stderr,
            stderr=sys.stderr,
        )

    # Attempt 1: anonymous, plus a cookies file if configured (domain-scoped,
    # safe for public sites too).
    result = run(_cookie_file_args())
    video = _pick_video(out_dir)

    # Attempt 2 (rescue): browser cookies, only when the first attempt produced
    # no file and a browser is configured. Requires that browser to be closed.
    if video is None:
        browser = _cookie_browser_args()
        if browser:
            print(
                "[watch] anonymous download produced no file; retrying with browser cookies…",
                file=sys.stderr,
            )
            result = run(_cookie_file_args() + browser)
            video = _pick_video(out_dir)

    if video is None:
        raise SystemExit(
            f"yt-dlp did not produce a video file in {out_dir} (exit {result.returncode}). "
            "For a login-walled source (Facebook/Instagram) set WATCH_COOKIES_FILE to a "
            "Netscape cookies.txt, or WATCH_COOKIES_BROWSER with that browser closed."
        )

    subtitle = _pick_subtitle(out_dir)
    info = _read_info(out_dir / "video.info.json", url)

    return {
        "video_path": str(video),
        "subtitle_path": str(subtitle) if subtitle else None,
        "info": info or {"url": url},
        "downloaded": True,
    }


def download(
    source: str,
    out_dir: Path,
    audio_only: bool = False,
) -> dict:
    if is_url(source):
        return download_url(source, out_dir, audio_only=audio_only)
    return resolve_local(source)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: download.py <url-or-path> <out-dir>", file=sys.stderr)
        raise SystemExit(2)
    result = download(sys.argv[1], Path(sys.argv[2]))
    print(json.dumps(result, indent=2))
