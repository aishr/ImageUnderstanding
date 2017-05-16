import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pylab import cm

def random(img, cmap):
    img = cv2.imread(img)
    img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    final = laplacian/255
    #final = cmap(laplacian)
    cv2.imshow("haha", final)


if __name__ == '__main__':
    random("images/mug1.jpg",cm.gray)

