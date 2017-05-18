import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pylab import cm

keptImage = None

def random(image):
    
    img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    x = len(img)
    y = len(img[0])

    DP = [[]]

    for i in range(y):
        DP[0].append(img[0][i])
    for i in range(1,x):
        DP.append([])
        for j in range(y):
            DP[i].append(0)
    for i in range(1,x):
        for j in range(y):
            if j == 0:
                DP[i][j] = min(DP[i-1][j], DP[i-1][j+1]) + img[i][j]
            elif j == y-1:
                DP[i][j] = min(DP[i-1][j-1], DP[i-1][j]) + img[i][j]
            else:
                DP[i][j] = min(DP[i-1][j-1], DP[i-1][j], DP[i-1][j+1]) + img[i][j]

    min1 = 100000000000000000
    index = 0
    for i in range(y):
        if DP[x-1][i] < min1:
            min1 = DP[x-1][i]
            index = i

    S = [index]
    a = x-1
    b = index
    while a > 0:
        if b > 0 and (DP[a][b] - img[a][b]) == DP[a-1][b-1]:
            S.append(b)
            a -= 1
            b -= 1
        elif b < y-1 and (DP[a][b] - img[a][b]) == DP [a-1][b+1]:
            S.append(b)
            a -= 1
            b += 1
        else:
            S.append(b)
            a -= 1
    new_img = np.zeros((x,y-1,3), np.uint8)
    path = S[::-1]
    for i in range(x):
        temp_lst = []
        for j in range(len(img[i])):
            if j != path[i]:
                temp_lst.append(image[i][j])
            else:
                img[i][j] = 0
        new_img[i] = np.array(temp_lst)          

    cv2.imshow("test", new_img)
    return new_img
if __name__ == '__main__':
    image = cv2.imread("scene5.jpg")
    cv2.imshow("original", image)
    for i in range(100):
        temp = random(image)
        image = temp
        

