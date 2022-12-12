# import cv2
# import matplotlib.pyplot as plt
#
# img = cv2.imread("img1.png")
# cv2.imshow('original img',img)
# print(img.shape)
# # scale_up_x = 1.2
# # scale_up_y = 1.2
# # # Scaling Down the image 0.8 times specifying a single scale factor.
# scale_down = 0.8
# scale_down1 = 0.8
# #
# scaled_f_down = cv2.resize(img, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)
# # scaled_f_up = cv2.resize(image, None, fx=scale_up_x, fy=scale_up_y, interpolation=cv2.INTER_LINEAR)
# print("resized img,",scaled_f_down.shape)
# scaled_f_down1 = cv2.resize(scaled_f_down, None, fx=scale_down1, fy=scale_down1, interpolation=cv2.INTER_LINEAR)
# cv2.imshow('new',scaled_f_down)
# cv2.imshow('new1',scaled_f_down)
# print("resized img,",scaled_f_down1.shape)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("img1.png")
cv2.imshow('original img',img)
print(img.shape)
layer=img.copy()
print(layer.shape)
ig=[layer]
for i in range(0,12):
    scale_down = 0.8
    layer1 = cv2.resize(layer, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)
    ig.append(layer)
    cv2.imshow(str(i), layer)
    layer=layer1.copy()
cv2.waitKey(0)
cv2.destroyAllWindows()



