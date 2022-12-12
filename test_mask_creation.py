import cv2
import numpy as np
import math
##gabor filter for value theata=0
#next create a loop for value theata=0 to pi with 17 orientation next file
arr=[]
for x in range(-5,5):
    theata=0
    gam=0.3
    sig=4.1
    lam=5.2
    for y in range(-6,6):
        m = x*(math.cos(theata))-y*(math.sin(theata))
        n= x*(math.cos(theata))+y*(math.sin(theata))
        g=math.exp((-((math.pow(m,2)+(math.pow(gam,2))*(math.pow(n,2)))/(2*math.pow(sig,2)))*math.cos(((2*math.pi)/lam)*m)))
        arr.append(g)
arr1=np.array(arr)
print(arr1)

