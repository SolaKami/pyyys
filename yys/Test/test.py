import time
import win32api
import win32gui

import win32con

# start




hwnd = win32gui.FindWindow(0,"阴阳师-网易游戏")
win32gui.SetForegroundWindow(hwnd)
win32gui.MoveWindow(hwnd,0,0,1152,650,True)
rt = win32gui.GetClientRect(hwnd)
str2 = u"%s, %d, %d, %d, %d" %(str, rt[0], rt[1], rt[2], rt[3])
print(str2)
# win32api.MessageBox(win32con.NULL, str2, u'Hello Python, 你好呀!', win32con.MB_OK)

# win32api.SendMessage(0)
# time.sleep(1)
# mouse.lefClick(100,100)
# win.mouse_click(100,100)

# core.startpve()


def click1(x, y):  # 第一种
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def click2(x, y):  # 第二种
    time.sleep(5)
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)


def click_it(pos):  # 第三种
    handle = win32gui.WindowFromPoint(pos)
    client_pos = win32gui.ScreenToClient(handle, pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)

def click3(x,y):
    handle = win32gui.FindWindow(0, "阴阳师-网易游戏")
    tmp = win32api.MAKELONG(x,y)
    win32gui.SetForegroundWindow(handle)
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)



