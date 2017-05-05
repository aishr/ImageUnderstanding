import cv2
import numpy as np
from collections import Counter
from colour import hex2web
import matplotlib
def makeDictionary():
    fd = open("dictionary.txt")
    lst = fd.readlines()
    dic = {}
    for i in range(len(lst)):
        lst[i] = lst[i].strip().split(":")
    for line in lst:
        dic[line[0]] = line[1]
    fd.close()
    return dic
def detectColour(imageName, backgroundColourSum, numOfColours):
    dic = makeDictionary()
    image = cv2.imread(imageName)
    #gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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
    a = dict(matplotlib.colors.cnames.items())
    for k in list(a):
        if a[k] != k:
            a[a[k]] = k
            del a[k]
    hex_dict = a
    blank_image = np.zeros((100,(numOfColours*50),3), np.uint8)
    x = Counter(hex_values).most_common(numOfColours)
    for i in range(numOfColours):
        colour = [int(x[i][0][2:4],16), int(x[i][0][4:6],16), int(x[i][0][6:8],16)]
        blank_image[:,(i*50):((i+1)*50)-1] = tuple(colour)
##    print(x[0][0][6:8] + " " + x[0][0][4:6] + " " + x[0][0][2:4])
    R = 51 * ((int(x[0][0][6:8], 16) + 25)//51)
    G = 51* ((int(x[0][0][4:6], 16) + 25)//51)
    B = 51 * ((int(x[0][0][2:4], 16) + 25) //51)
    print(str(R) + " " + str(G) + " " + str(B))
    key = hex(R)[2:]+ hex(G)[2:]+hex(B)[2:]
    final_colour = dic[key]
##    if R > G:
##        if R > B:
##            if R > 128:
##                if abs(G-B) <= 30 and abs(R-G) <= 45:
##                    final_colour = "PINK"
##                else:
##                    final_colour = "RED"
##            elif R > 16:
##                if abs(G-B) <=10:
##                    final_colour = "BLACK"
##                else:
##                    final_colour = "BROWN"
##            else:
##                final_colour = "BLACK"
##        elif R == B:
##            if R >= 238:
##                final_colour = "PINK"
##            else:
##                final_colour = "PURPLE"
##        else:
##            if B <= 16:
##                final_colour = "BLACK"
##            else:
##                final_colour = "BLUE"
##    elif R == G:
##        if R >= 112:
##            final_colour = "YELLOW"
##        elif R >= 16:
##            final_colour = "BROWN"
##        else:
##            final_colour = "BLACK"
##    else:
##        if G > B:
##            if G > 16:
##                final_colour = "GREEN"
##            else:
##                final_colour = "BLACK"
##        elif G == B:
##            if G >= 16:
##                final_colour = "BLUE"
##            else:
##                final_colour = "BLACK"
##        else:
##            if B >= 16:
##                final_colour = "BLUE"
##            else:
##                final_colour = "BLACK"
##    if abs(R-G) <=20 and abs(G-B) <=20:
##        final_colour = "BLACK"
                
    cv2.imshow(final_colour, image)
    cv2.imshow("palette", blank_image)
    
detectColour("box.jpg", 765, 10)

'''
Black: 00-00-00 : 
Brown 05-00-00 : 7f-00-00
Red: 80-00-00 : ff-00-00
Green: 00-20-00 : 00-ff-00
Pink: b83850 - 
'''
        
        
