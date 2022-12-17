import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# from new_multiscale import *
import new_multiscale

digits=load_digits()
print(list(digits))
# # #feature extraction
img=0
x=new_multiscale.hand_palm_rec(img)
# x2=digits.images.reshape(len(digits.images),-1)
# print("size of x",x.shape)
y=digits.target
print("size of y",y.shape)

#for Training data
gabor=[]# for x_train
y_1=[]# for y_train
for i in range(0,5000):
   arr = x[i].astype('uint8')
   gabor=new_multiscale.hand_palm_rec(arr)
   for j in gabor:
      s=[]
      s.append(j[0])
      gabor.append(s)
      y_1.append(y[i])
x_train=np.array(gabor)
y_train=np.array(y_1)
print(x_train.shape)
print(y_train.shape)

# #for testing data
# hist_append_test=[]# for x_test
# y_test=[]# for y_test
# for i in range(1501,1697):
#     arr = x[i].astype('uint8')
#     hist=cv2.calcHist([arr],[0],None,[30],[0,16])
#
#     for j in hist:
#         s1=[]
#         s1.append(j[0])
#     hist_append_test.append(s1)
#     y_test.append(y[i])
# x_test=np.array(hist_append_test)
# y_test=np.array(y_test)
# print(x_test.shape)
# print(y_test.shape)
# # plt.title('Image Histogram')
# # plt.show()
#
# ##USING SVC
# model=SVC(kernel="rbf",random_state=0)
# model.fit(x_train,y_train)
# # # #
# # # # #Accuracy
# y_pred=model.predict(x_test)
# # y_pred=model.predict(x_train)
#
#
# #
# accuracy=accuracy_score(y_test,y_pred)
# print('ACCURACY is',accuracy)
# # #
# print("training score=",model.score(x_train,y_train))
# print("testing score=",model.score(x_test,y_test))
# # #
# # # a=int(input("enter the digit you want to predict"))
# # plt.gray()
# # plt.imshow(digits.images[a])
# # plt.title('Orignal it is: '+str(digits.target[a]))
# # plt.show()
# # # # #
# # # #
# #
# # ##prediction testing
# # print("!!!!!!For Testing")
# # prediction=model.predict(x_test[100].reshape(1,-1))
# # print("prediction value=",prediction)
# # print("target value=",y[100])#
# # ##USING lOGISTIC REGRESRESSION
# # lr=LogisticRegression()
# # lr.fit(x_train,y_train)
# # ##Model Prediction
# # y_pred=lr.predict(x_test)
# # print(y_pred)
# #
# # ##Accuracy Checking
# # accuracy=accuracy_score(y_test,y_pred)
# # print("!!!!!!!Accuracy by using Logistic Regression")
# # print("Accuracy using Logistic Regression",accuracy)
