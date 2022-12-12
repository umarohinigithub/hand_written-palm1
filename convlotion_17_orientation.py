import cv2
import numpy as np
import math

#next create a loop for value theata=0 to pi with 17 orientation
arr = [[0]*13]*11##11 row and 13 columns
ar=np.array(arr)
for theata in np.arange(0, 180, 11):

    for x in range(-5,5):

        gam=0.3
        sig=4.1
        lam=5.2
        for y in range(-6,6):
            m = x*(math.cos(theata))-y*(math.sin(theata))
            n= x*(math.cos(theata))+y*(math.sin(theata))
            g=math.exp((-((math.pow(m,2)+(math.pow(gam,2))*(math.pow(n,2)))/(2*math.pow(sig,2)))*math.cos(((2*math.pi)/lam)*m)))

        print(ar[x+x][y+y],[x,y])

