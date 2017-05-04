import cv2
import numpy as np
from collections import Counter
from colour import hex2web


def detectColour(imageName, backgroundColourSum, numOfColours):
    image = cv2.imread(imageName)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    colour_list = []

    for i in range(len(image)):
        for j in range(len(image[i])):
            num_sum = sum(image[i][j])
            if num_sum <= backgroundColourSum - 60:
                colour_list.append(image[i][j])
    hex_values = []
    for i in range(len(colour_list)):
        hex_num = ''
        for j in range(len(colour_list[i])):
            if j > 0:
                hex_num = hex_num + hex(colour_list[i][j])[2:]
            else:
                hex_num = hex_num + hex(colour_list[i][j])
        hex_values.append(hex_num)
        
    blank_image = np.zeros((100,(numOfColours*50),3), np.uint8)
    x = Counter(hex_values).most_common(numOfColours)
    for i in range(numOfColours):
        colour = [int(x[i][0][2:4],16), int(x[i][0][4:6],16), int(x[i][0][6:8],16)]
        blank_image[:,(i*50):((i+1)*50)-1] = tuple(colour)

    cv2.imshow("image", image)
    cv2.imshow("test", blank_image) 
    

detectColour("box.jpg", 765, 20)
        
        
