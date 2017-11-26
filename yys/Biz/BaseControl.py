import os
import cv2
from PIL import ImageGrab
from BaseLib import PictureMatch as pm
from BaseLib import  Mouse

# define global parameter
PICTURE_DIR = os.path.dirname(os.getcwd()) + "\\Resource\\"
SCREENTSHOT_NAME = '\\1.png'

# find & click
def click_pic(pic):
    save_screentshot()
    img = get_image(SCREENTSHOT_NAME)
    template = get_image("\\" + pic+".png")
    x, y = pm.match(img, template)
    if x > 0:
        move_and_click(x, y)
    else:
        return 0


def has_pic(pic):
    save_screentshot()
    img = get_image(SCREENTSHOT_NAME)
    template = get_image("\\"+pic+".png")
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
    return

def save_screentshot():
    im = ImageGrab.grab()
    im.save(PICTURE_DIR + SCREENTSHOT_NAME)
    return