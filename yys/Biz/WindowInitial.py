import win32con
import win32api
import win32gui
import win32com.client

def ini_game_window(name):
    hwnd = win32gui.FindWindow(0, name)
    win32gui.SetForegroundWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 1152, 650, True)
    return

def set_window_top(name):
    hwnd = win32gui.FindWindow(0, name)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(hwnd)
    return


def close_window(name):
    hwnd = win32gui.FindWindow(0, name)
    win32gui.PostMessage(hwnd,win32con.WM_CLOSE,0,0)
    #win32gui.CloseWindow(hwnd)
    return