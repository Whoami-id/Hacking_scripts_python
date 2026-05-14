from ctypes import *
from ctypes.wintypes import HWND, LPCSTR, UINT, INT, LPSTR, LPDWORD, DWORD, HANDLE, BOOL



MessageBoxA = windll.user32.MessageBoxA
MessageBoxA.argtypes = [HWND, LPCSTR, LPCSTR, UINT]
MessageBoxA.restype = INT
print(MessageBoxA)

lpText = LPCSTR(b"World")
lpCaption = LPCSTR(b"Hello")
MB_OK = 0x00000000
MessageBoxA(None, lpText, lpCaption, MB_OK)

