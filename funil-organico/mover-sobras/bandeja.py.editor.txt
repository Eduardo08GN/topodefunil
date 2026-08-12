# -*- coding: utf-8 -*-
"""Icone na bandeja do Windows para o Veo Editor, sem dependencia nova.

Encomenda do operador (2026-08-11): *"quero que a interface do editor fique
persistente na tela, ao menos que eu a feche no X, dai ela vai por system
tray"*.

⛔ NAO USA `pystray`. O venv do editor nao tem, e instalar exigiria baixar
pacote numa ferramenta que ja' esta' em producao. Tudo aqui e' `ctypes` sobre a
API que o Windows ja' oferece — o mesmo `Shell_NotifyIcon` que todo programa de
bandeja usa.

⚠️ A JANELA DE MENSAGENS E' CRIADA NA THREAD DO TKINTER, de proposito. O laco do
Tk e' um laco de mensagens do Windows como qualquer outro: ele despacha as
mensagens de TODAS as janelas da thread, inclusive desta. Criar noutra thread
exigiria um segundo laco e abriria a porta para os travamentos classicos de GUI
em duas threads.

⚠️ E o icone e' REMOVIDO no fim. Icone fantasma na bandeja — daqueles que so'
somem quando o mouse passa por cima — e' o defeito mais comum desta API, e vem
de nao chamar NIM_DELETE ao sair.
"""
import ctypes
import os
from ctypes import wintypes

user32 = ctypes.windll.user32
shell32 = ctypes.windll.shell32
kernel32 = ctypes.windll.kernel32

WM_USER = 0x0400
WM_BANDEJA = WM_USER + 20
WM_LBUTTONUP = 0x0202
WM_LBUTTONDBLCLK = 0x0203
WM_RBUTTONUP = 0x0205
WM_DESTROY = 0x0002
WM_COMMAND = 0x0111

NIM_ADD, NIM_MODIFY, NIM_DELETE = 0, 1, 2
NIF_MESSAGE, NIF_ICON, NIF_TIP = 0x01, 0x02, 0x04
IMAGE_ICON = 1
LR_LOADFROMFILE = 0x0010
TPM_RIGHTBUTTON = 0x0002
MF_STRING = 0x0000
MF_SEPARATOR = 0x0800

ID_ABRIR, ID_SAIR = 1001, 1002

WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_longlong, wintypes.HWND, wintypes.UINT,
                             wintypes.WPARAM, wintypes.LPARAM)

# ⛔⛔ DECLARAR OS TIPOS NAO E' ZELO, E' OBRIGATORIO EM 64 BITS. Sem isto o
# ctypes assume `int` de 32 bits para handles e ponteiros, e um HWND ou HINSTANCE
# de verdade nao cabe: o CreateWindowExW estourou com "int too long to convert"
# na primeira execucao deste arquivo. E o pior caso nao e' o erro — e' o handle
# TRUNCADO que passa silenciosamente e aponta para nada.
kernel32.GetModuleHandleW.restype = wintypes.HMODULE
kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]
user32.RegisterClassW.restype = wintypes.ATOM
user32.RegisterClassW.argtypes = [ctypes.c_void_p]
user32.CreateWindowExW.restype = wintypes.HWND
user32.CreateWindowExW.argtypes = [wintypes.DWORD, wintypes.LPCWSTR,
                                   wintypes.LPCWSTR, wintypes.DWORD,
                                   ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                   ctypes.c_int, wintypes.HWND, wintypes.HMENU,
                                   wintypes.HINSTANCE, wintypes.LPVOID]
user32.DefWindowProcW.restype = ctypes.c_longlong
user32.DefWindowProcW.argtypes = [wintypes.HWND, wintypes.UINT,
                                  wintypes.WPARAM, wintypes.LPARAM]
user32.LoadImageW.restype = wintypes.HANDLE
user32.LoadImageW.argtypes = [wintypes.HINSTANCE, wintypes.LPCWSTR,
                              wintypes.UINT, ctypes.c_int, ctypes.c_int,
                              wintypes.UINT]
user32.LoadIconW.restype = wintypes.HICON
user32.LoadIconW.argtypes = [wintypes.HINSTANCE, wintypes.LPCWSTR]
user32.CreatePopupMenu.restype = wintypes.HMENU
user32.AppendMenuW.argtypes = [wintypes.HMENU, wintypes.UINT,
                               ctypes.c_void_p, wintypes.LPCWSTR]
user32.TrackPopupMenu.argtypes = [wintypes.HMENU, wintypes.UINT, ctypes.c_int,
                                  ctypes.c_int, ctypes.c_int, wintypes.HWND,
                                  ctypes.c_void_p]
user32.DestroyMenu.argtypes = [wintypes.HMENU]
user32.SetForegroundWindow.argtypes = [wintypes.HWND]
user32.PostMessageW.argtypes = [wintypes.HWND, wintypes.UINT,
                                wintypes.WPARAM, wintypes.LPARAM]
shell32.Shell_NotifyIconW.restype = wintypes.BOOL
shell32.Shell_NotifyIconW.argtypes = [wintypes.DWORD, ctypes.c_void_p]


class WNDCLASS(ctypes.Structure):
    _fields_ = [("style", wintypes.UINT), ("lpfnWndProc", WNDPROC),
                ("cbClsExtra", ctypes.c_int), ("cbWndExtra", ctypes.c_int),
                ("hInstance", wintypes.HINSTANCE), ("hIcon", wintypes.HICON),
                ("hCursor", wintypes.HANDLE), ("hbrBackground", wintypes.HBRUSH),
                ("lpszMenuName", wintypes.LPCWSTR), ("lpszClassName", wintypes.LPCWSTR)]


class NOTIFYICONDATA(ctypes.Structure):
    _fields_ = [("cbSize", wintypes.DWORD), ("hWnd", wintypes.HWND),
                ("uID", wintypes.UINT), ("uFlags", wintypes.UINT),
                ("uCallbackMessage", wintypes.UINT), ("hIcon", wintypes.HICON),
                ("szTip", wintypes.WCHAR * 128), ("dwState", wintypes.DWORD),
                ("dwStateMask", wintypes.DWORD), ("szInfo", wintypes.WCHAR * 256),
                ("uTimeout", wintypes.UINT), ("szInfoTitle", wintypes.WCHAR * 64),
                ("dwInfoFlags", wintypes.DWORD)]


class Bandeja:
    """Icone na bandeja. `ao_abrir` e `ao_sair` sao chamados na thread do Tk."""

    def __init__(self, titulo, icone=None, ao_abrir=None, ao_sair=None):
        self.titulo = titulo[:127]
        self.ao_abrir = ao_abrir or (lambda: None)
        self.ao_sair = ao_sair or (lambda: None)
        self._vivo = False

        self._proc = WNDPROC(self._wndproc)      # ⚠️ guardado: se o Python
        cls = WNDCLASS()                         # coletar isto, o Windows chama
        cls.lpfnWndProc = self._proc             # um ponteiro morto e o app cai
        cls.lpszClassName = "VeoEditorBandeja"
        cls.hInstance = kernel32.GetModuleHandleW(None)
        self._atom = user32.RegisterClassW(ctypes.byref(cls))
        self.hwnd = user32.CreateWindowExW(0, cls.lpszClassName, self.titulo,
                                           0, 0, 0, 0, 0, None, None,
                                           cls.hInstance, None)

        self.hicon = None
        if icone and os.path.isfile(icone):
            self.hicon = user32.LoadImageW(None, icone, IMAGE_ICON, 0, 0,
                                           LR_LOADFROMFILE)
        if not self.hicon:
            self.hicon = user32.LoadIconW(None, 32512)     # IDI_APPLICATION

    def mostrar(self):
        if self._vivo:
            return
        nid = self._dados()
        if shell32.Shell_NotifyIconW(NIM_ADD, ctypes.byref(nid)):
            self._vivo = True

    def esconder(self):
        if not self._vivo:
            return
        shell32.Shell_NotifyIconW(NIM_DELETE, ctypes.byref(self._dados()))
        self._vivo = False

    def _dados(self):
        nid = NOTIFYICONDATA()
        nid.cbSize = ctypes.sizeof(NOTIFYICONDATA)
        nid.hWnd = self.hwnd
        nid.uID = 1
        nid.uFlags = NIF_MESSAGE | NIF_ICON | NIF_TIP
        nid.uCallbackMessage = WM_BANDEJA
        nid.hIcon = self.hicon
        nid.szTip = self.titulo
        return nid

    def _menu(self):
        m = user32.CreatePopupMenu()
        user32.AppendMenuW(m, MF_STRING, ID_ABRIR, "Abrir o Veo Editor")
        user32.AppendMenuW(m, MF_SEPARATOR, 0, None)
        user32.AppendMenuW(m, MF_STRING, ID_SAIR, "Sair")
        pt = wintypes.POINT()
        user32.GetCursorPos(ctypes.byref(pt))
        # ⚠️ SetForegroundWindow antes do menu: sem isso o menu da bandeja fica
        # aberto e nao fecha ao clicar fora — comportamento documentado da API.
        user32.SetForegroundWindow(self.hwnd)
        user32.TrackPopupMenu(m, TPM_RIGHTBUTTON, pt.x, pt.y, 0, self.hwnd, None)
        user32.PostMessageW(self.hwnd, 0, 0, 0)
        user32.DestroyMenu(m)

    def _wndproc(self, hwnd, msg, wparam, lparam):
        if msg == WM_BANDEJA:
            if lparam in (WM_LBUTTONUP, WM_LBUTTONDBLCLK):
                self.ao_abrir()
            elif lparam == WM_RBUTTONUP:
                self._menu()
            return 0
        if msg == WM_COMMAND:
            cmd = wparam & 0xFFFF
            if cmd == ID_ABRIR:
                self.ao_abrir()
            elif cmd == ID_SAIR:
                self.ao_sair()
            return 0
        if msg == WM_DESTROY:
            self.esconder()
            return 0
        return user32.DefWindowProcW(hwnd, msg, wparam, lparam)
