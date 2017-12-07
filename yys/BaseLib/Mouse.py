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

def db_click(x,y):
    m = PyMouse()
    m.move(x,y)
    m.click(x,y,1)
    m.click(x, y, 1)
    return

def slide_up(x,y,h):


    m = PyMouse()
    m.move(x, y)
    #m.press(x, y, 1)
    #m.move(x, y - h)
    #m.release(x, y - h, 1)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -h)

    return

def slide_down(x,y,h):
    m = PyMouse()
    m.move(x, y)
    m.press(x, y, 1)
    m.move(x, y + h)
    m.release(x, y + h, 1)
    return

def move(x,y):
    m = PyMouse()
    m.move(x, y)
    return

def move_from_to(x1,y1,x2,y2):
    y=int((y2-y1)/20)
    x=int((x2-x1)/20)
    m = PyMouse()
    m.move(x1, y1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    num = 1
    while num <= 18:
        num += 1
        x2=x1+x*num
        y2=y1+y*num
        time.sleep(0.05)
        m.move(x2,y2)
        print("moveto  %d  %d"%(x2,y2))
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    return
#
# x1=700
# y1=700
# x2=100
# y2=100
# y=int((y2-y1)/10)
# x=int((x2-x1)/10)
# num = 1
# while num<10:
#     num +=1
#     x2 = x1 + x * num
#     y2 = y1 + y * num
#     print("num %d"%num)
#     print("x2 %d y2 %d"%(x2,y2))