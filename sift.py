import cv2
import numpy as np
from scipy.ndimage.filters import gaussian_filter as gs
from scipy.ndimage.filters import maximum_filter as mf

def imregionalmax(img):
    keypoints = []
    for i in range(len(img)):
        for j in range(len(img[i])):
            if i > 0 and i < len(img)-1 and j > 0 and j < len(img[i]) -1:
                test = []
                test.append(img[i-1][j-1])
                test.append(img[i-1][j])
                test.append(img[i-1][j+1])
                test.append(img[i][j-1])
                test.append(img[i+1][j+1])
                test.append(img[i+1][j-1])
                test.append(img[i+1][j])
                test.append(img[i+1][j+1])
                #print("pixel: " + str(img[i][j]))
                #print("max: " + str(max(test)))
                if img[i][j] > max(test):
                    keypoints.append((i,j))
    print(len(keypoints))            
    return keypoints
                
                
def sift(spo,sigma):
    img = cv2.imread('ColourDetector/images/mug1.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    threshold = 0.4
    n = 1
    x = 1
    for i in range(1):
        while len(img[0]) > 40:
            one = gs(gray, sigma)
            val = sigma * ((2**(1//spo))^1)
            two = gs(gray,val)
            result = two-one
            one = two[:]
            cv2.imshow("result",result)
            print(result[:5][:5])

            keypoints = imregionalmax(result)

            
            #for i in range(len(keypoints)):
            #    cv2.circle(img,keypoints[i][::-1], 5, (0,0,255))
            #cv2.imshow("img",img)
        
##    for i in range(0,100,10):
##        cv2.circle(img,(100+i,100+i), 5, (250,0,0))


sift(10,4)
    
