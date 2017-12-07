import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


def match(img2,template2):
    template=template2.copy()
    w, h = template.shape[::-1]
    x=0
    y=0
    value=0
    # 6 中匹配效果对比算法
    methods = ['cv2.TM_CCOEFF_NORMED']

    # methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        img = img2.copy()

        method = eval(meth)

        res = cv2.matchTemplate(img, template, method)

        # loc = np.where(res>=0.989)
        # rs = list(zip(*loc))
        # if len(rs) == 0:
        #     raise ItemNotFound

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
            value=min_val
        else:
            top_left = max_loc
            value=max_val

        # print(min_val)
        # print(max_val)
        # value = min_val/max_val



        x = int(top_left[0]+w/2)
        y = int(top_left[1]+h/2)


        # print(x)
        # print(y)
        #bottom_right = (top_left[0] + w, top_left[1] + h)
        # cv2.rectangle(img, top_left, bottom_right, 255, 2)
        # print
        # meth
        # plt.subplot(221), plt.imshow(img2, cmap="gray")
        # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        # plt.subplot(222), plt.imshow(template, cmap="gray")
        # plt.title('template Image'), plt.xticks([]), plt.yticks([])
        # plt.subplot(223), plt.imshow(res, cmap="gray")
        # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        # plt.subplot(224), plt.imshow(img, cmap="gray")
        # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        # plt.show()
    # print(value)
    if value > 0.9:
        return x, y
    else:
        return 0, 0
