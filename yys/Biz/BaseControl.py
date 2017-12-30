import os
import cv2
from PIL import ImageGrab
from BaseLib import PictureMatch as pm
from BaseLib import Mouse
import numpy as np
import  time

# define global parameter
PICTURE_DIR = os.path.dirname(os.getcwd()) + "\\Resource\\"
SCREENTSHOT_NAME = '\\1.png'

# find & click
def click_pic(pic):
    #save_screentshot()
    #img = get_image(SCREENTSHOT_NAME)
    im = ImageGrab.grab((0, 0, 1200, 800))
    img= np.array(im.convert('L'))
    template = get_image("\\" + pic+".png")
    x, y = pm.match(img, template)
    if x > 0:
        move_and_click(x, y)
        return 1
    else:
        return 0

def db_click_pic(pic):
    #save_screentshot()
    # img = get_image(SCREENTSHOT_NAME)
    im = ImageGrab.grab((0, 0, 1200, 800))
    img = np.array(im.convert('L'))
    template = get_image("\\" + pic+".png")
    x, y = pm.match(img, template)
    if x > 0:
        Mouse.db_click(x,y)
        print("double click")
        return 1
    else:
        return 0

def click_pic_plus(pic,a,b):
    #save_screentshot()
    # img = get_image(SCREENTSHOT_NAME)
    im = ImageGrab.grab((0, 0, 1200, 800))
    img = np.array(im.convert('L'))
    template = get_image("\\" + pic+".png")
    x, y = pm.match(img, template)
    if x > 0:
        move_and_click(x+a, y+b)
        return 1
    else:
        return 0

def slide_up(pic,h):
    #save_screentshot()
    # img = get_image(SCREENTSHOT_NAME)
    im = ImageGrab.grab((0, 0, 1200, 800))
    img = np.array(im.convert('L'))
    template = get_image("\\" + pic+".png")
    x, y = pm.match(img, template)
    if x > 0:
        Mouse.slide_up(x, y,h)
        return 1
    else:
        return 0

def move_from_to(pic1,pic2):
    im1 = ImageGrab.grab((0, 0, 1200, 800))
    im2 = ImageGrab.grab((400, 0, 1200, 800))
    img1 = np.array(im1.convert('L'))
    img2 = np.array(im2.convert('L'))
    template1 = get_image("\\" + pic1 + ".png")
    template2 = get_image("\\" + pic2 + ".png")
    x1, y1 = pm.match(img1, template1)
    x2, y2 = pm.match(img2, template2)
    if x2>0:
        x2 += 400
    print("x1:%d y1:%d x2:%d y2:%d"%(x1,y1,x2,y2))
    # Mouse.move(x1,y1)
    # raise
    if x1>0 and x2>0:
        Mouse.move_from_to(x1,y1,x2,y2)
        return 1
    else:
        return 0


def has_pic(pic):
    #save_screentshot()
    # img = get_image(SCREENTSHOT_NAME)
    im = ImageGrab.grab((0, 0, 1200, 800))
    img = np.array(im.convert('L'))
    template = get_image("\\" + pic + ".png")
    x, y = pm.match(img, template)
    if x > 0:
        return 1
    else:
        return 0
def has_pic_plus(pic,a,b,c,d):
    im = ImageGrab.grab((a, b, c, d))
    img = np.array(im.convert('L'))
    template = get_image("\\" + pic + ".png")
    x, y = pm.match(img, template)
    if x > 0:
        return 1
    else:
        return 0


def get_image(img_name):
    str = PICTURE_DIR + img_name
    # print("image addr is :",str)
    img = cv2.imread(str, 0)
    return img

def move_and_click(x, y):
    Mouse.lefClick(x, y)
    time.sleep(1)
    return

def save_screentshot():
    im = ImageGrab.grab((0, 0, 1200, 800))
    im.save(PICTURE_DIR + SCREENTSHOT_NAME)
    return