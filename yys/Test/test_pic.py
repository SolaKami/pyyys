import os
import cv2
from PIL import ImageGrab
from BaseLib import PictureMatch as pm
from BaseLib import  Mouse
import numpy as np


img = ImageGrab.grab((0, 0, 1200, 800))
im = np.array(img.convert('RGB'))
cv2.imshow('lena',im)
cv2.waitKey(0)