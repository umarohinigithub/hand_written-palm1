import cv2
import matplotlib.pyplot as plt
import numpy as np
import skimage.measure
from test_filter import *


def hand_palm_rec(img):
    color_img = cv2.imread("img1.png")
    img = cv2.cvtColor(color_img,cv2.COLOR_BGR2GRAY)
    # cv2.imshow('original img',img)
    # print('shape of original image=',img.shape)
    layer=img.copy()
    ig=[layer]
    rows=[]
    image=[]
    for i in range(0,12):
        scale_down = 0.8
        layer1 = cv2.resize(layer, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)
        ig.append(layer)
        layer=layer1.copy()
        gfilters = create_gaborfilter()
        g = np.array(gfilters)
        image_g = apply_filter(layer, gfilters)
        image.extend(image_g)
    return image




#
#
