from pymouse import PyMouse
from pykeyboard import PyKeyboard
import  time
import win32api
import win32con

def lefClick(x,y):
    m = PyMouse()
    m.move(x,y)
    m.click(x,y,1)
    return

def slide_up(x,y,h):


    m = PyMouse()
    m.move(x, y)
    #m.press(x, y, 1)
    #m.move(x, y - h)
    #m.release(x, y - h, 1)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -500)

    return

def slide_down(x,y,h):
    m = PyMouse()
    m.move(x, y)
    m.press(x, y, 1)
    m.move(x, y + h)
    m.release(x, y + h, 1)
    return
