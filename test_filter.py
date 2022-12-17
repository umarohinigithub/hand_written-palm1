import cv2
import numpy as np
import skimage.measure
n_image=[]

def create_gaborfilter():
    filters = []
    num_filters = 17
    ksize1 = 11  # The local area to evaluate
    ksize2 = 13
    sigma = 4.1  # Larger Values produce more edges
    lambd = 5.2
    gamma = 0.3
    psi = 0  # Offset value - lower generates cleaner results
    for theta in np.arange(0, 180 / num_filters):  # Theta is the orientation for edge detection
        kern = cv2.getGaborKernel((ksize1, ksize2), sigma, theta, lambd, gamma, psi, ktype=cv2.CV_64F)
        # print(kern)
        kern /= 1.0 * kern.sum()  # Brightness normalization
            # print('size of kern',kern.shape)
        filters.append(kern)
    return filters
def apply_filter(layer, filters):
    rows=[]
    newimage = np.zeros_like(layer)
    depth = -1  # remain depth same as original image
    for kern in filters:  # Loop through the kernels in our GaborFilter
        image_filter = cv2.filter2D(layer, depth, kern)  # Apply filter to image
        cv2.imshow('image',image_filter)
        # cv2.waitKey(0)
        # new=np.maximum(layer, image_filter, newimage)
        mp = skimage.measure.block_reduce(image_filter, (10, 10), np.mean)
        row = mp.flatten()  ##flatten is used to convert all elements of matrix into single row
        rows.extend(row)
        # n_image.append(new)

    return rows