import win32con
import win32api
import win32gui

def ini_game_window():
    hwnd = win32gui.FindWindow(0, "阴阳师-网易游戏")
    win32gui.SetForegroundWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 1152, 650, True)
    return

def set_window_top():
    hwnd = win32gui.FindWindow(0, "阴阳师-网易游戏")
    win32gui.SetForegroundWindow(hwnd)
    return