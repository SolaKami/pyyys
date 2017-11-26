from pymouse import PyMouse
from pykeyboard import PyKeyboard
import  time

def lefClick(x,y):
    m = PyMouse()
    m.move(x,y)
    m.click(x,y,1)
    return
