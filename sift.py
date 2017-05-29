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
    return keypoints

def arrayMax(lst):
    tempMax = []
    for line in lst:
        tempMax.append(max(line))
    return max(tempMax)

def sift(spo,sigma):
    img = cv2.imread('ColourDetector/images/mug1.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    finalimg = img[:]
    threshold = 0.2
    n = 1
    x = 1
    while len(img[0]) > 40:
        one = gs(gray, sigma)
        val = sigma * ((2**(1/spo))**1)
        print("value: " + str(val))
        two = gs(gray,val)
        result = two-one
        one = two[:]
        final = np.zeros((len(result), len(result[0])))

        keypoints = imregionalmax(result)

        keyp = np.zeros((len(result),len(result[0])))

        maxKeyP = arrayMax(result)
        
        for i in range(len(keyp)):
            for j in range(len(keyp[0])):
                if (i,j) in keypoints and (result[i][j]/maxKeyP) > threshold:
                    keyp[i][j] = result[i][j]
                elif (i,j) in keypoints:
                    keypoints.remove((i,j))
        pending = keyp[:]
        cv2.imshow("pending", pending)

        for i in range(1,spo):
            val = sigma * ((2**(1/spo))**i)
            print(val)
            two = gs(gray,val)
            result = two-one
            one = two[:]

            keypoints = imregionalmax(result)

            keyp = np.zeros((len(result),len(result[0])))

            maxKeyP = arrayMax(result)
            
            for k in range(len(keyp)):
                for j in range(len(keyp[0])):
                    if (k,j) in keypoints and (result[k][j]/maxKeyP) > threshold:
                        keyp[k][j] = result[k][j]
                    elif (k,j) in keypoints:
                        keypoints.remove((k,j))

            for point in keypoints:
                if keyp[point[0]][point[1]] <= pending[point[0]][point[1]]:
                    final[point[0]][point[1]] = 1
                    print("hi")
                else:
                    pending[point[0]][point[1]] = keyp[point[0]][point[1]]
        for i in range(len(final)):
            for j in range(len(final[0])):
                if final[i][j] == 1:
                    cv2.circle(finalimg,(i*n,j*n), x*sigma, (0,0,255))
        img = cv2.pyrDown(img)
        n = n*2
        x = x+1
        '''
        for i in range(len(keypoints)):
            cv2.circle(img,keypoints[i][::-1], 5, (0,0,255))
        '''
    cv2.imshow("final", finalimg)
sift(5,4)
    
