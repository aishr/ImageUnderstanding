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

def webSafeColour(num):
    num = int(num,16)
    num = 51 * ((num + 25)//51)
    num = hex(num)[2:]
    if len(num) != 2:
        num = '0' + num
    return num
def findTopColour(imageName, colourCode):
    image = cv2.imread(imageName)
    
def detectColour(imageName, backgroundColourSum, numOfColours):
    dic = makeDictionary()
    image = cv2.imread(imageName)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    colour_list = []

    for i in range(len(image)):
        for j in range(len(image[i])):
            num_sum = sum(image[i][j])
            if num_sum <= backgroundColourSum - 60:
                colour_list.append(image[i][j])
##                image[i][j] = [0,0,0]
##            else:
##                image[i][j] = [0,0,0]
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
    cv2.imshow("image", image)
    x = Counter(hex_values).most_common(numOfColours)
    for i in range(numOfColours):
        if len(x[i][0]) != 8:
            x[i] = (x[i][0] + ((8 - len(x[i][0]))*'0'),x[i][1])
        print(x[i][0])
        colour = [int(x[i][0][2:4],16), int(x[i][0][4:6],16), int(x[i][0][6:8],16)]
        blank_image[:,(i*50):((i+1)*50)-1] = tuple(colour)
        R = webSafeColour(x[i][0][6:8])
##        print(R)
        print(x[i][0][6:8])
        G = webSafeColour(x[i][0][4:6])
##        print(G)
        print(x[i][0][4:6])
        B = webSafeColour(x[i][0][2:4])
##        print(B)
        print(x[i][0][2:4])
##        print(str(R) + " " + str(G) + " " + str(B))
        temp_key = R+G+B
        print(temp_key)
        print("Colour " + str(i+1) + ": " + dic[temp_key] + " Frequency: " + str(x[i][1]))
        
    R = webSafeColour(x[0][0][6:8])
##    print(R)
    G = webSafeColour(x[0][0][4:6])
##    print(G)
    B = webSafeColour(x[0][0][2:4])
##    print(B)
##    print(str(R) + " " + str(G) + " " + str(B))
   
    key = R+G+B
    print(key)
    final_colour = dic[key]

    cv2.imshow(final_colour, image)
    cv2.imshow("palette", blank_image)
    
detectColour("mug2.jpg", 765, 10)

'''
    if R > G:
        if R > B:
            if R > 128:
                if abs(G-B) <= 30 and abs(R-G) <= 45:
                    final_colour = "PINK"
                else:
                    final_colour = "RED"
            elif R > 16:
                if abs(G-B) <=10:
                    final_colour = "BLACK"
                else:
                    final_colour = "BROWN"
            else:
                final_colour = "BLACK"
        elif R == B:
            if R >= 238:
                final_colour = "PINK"
            else:
                final_colour = "PURPLE"
        else:
            if B <= 16:
                final_colour = "BLACK"
            else:
                final_colour = "BLUE"
    elif R == G:
        if R >= 112:
            final_colour = "YELLOW"
        elif R >= 16:
            final_colour = "BROWN"
        else:
            final_colour = "BLACK"
    else:
        if G > B:
            if G > 16:
                final_colour = "GREEN"
            else:
                final_colour = "BLACK"
        elif G == B:
            if G >= 16:
                final_colour = "BLUE"
            else:
                final_colour = "BLACK"
        else:
            if B >= 16:
                final_colour = "BLUE"
            else:
                final_colour = "BLACK"
    if abs(R-G) <=20 and abs(G-B) <=20:
        final_colour = "BLACK"
                
'''
        
        
