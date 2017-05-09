from cv2 import *
from numpy import *
from collections import Counter

def makeDictionary():
    fd = open("dictionary.txt")
    lst = fd.readlines()
    dic = {}
    for i in range(len(lst)):
        lst[i] = lst[i].strip().split(",")
    for line in lst:
        dic[line[0]] = line[1]
    fd.close()
    return dic

def RGB2Hex(rgb):
    hexNum = ''
    for num in rgb:
        if len(hex(num)) != 4:
            hexNum += "0"
        hexNum += hex(num)[2:]
    return hexNum

def webSafeColour(num):
    num = int(num,16)
    num = 51 * ((num + 25)//51)
    num = hex(num)[2:]
    if len(num) != 2:
        num = '0' + num
    return num

def detectColour(imageName):
    colourData = makeDictionary()
    image = imread(imageName)
    edges = Canny(image, 50, 150, 3)
    colourList = []
    backgroundColourSum = sum(image[0][0])

    for i in range(len(image)):
        for j in range(len(image[i])):
            numSum = sum(image[i][j])
            if numSum <= abs(backgroundColourSum - 60):
                hexValue = RGB2Hex(image[i][j])                
                webSafe = webSafeColour(hexValue[4:]) + webSafeColour(hexValue[2:4]) + webSafeColour(hexValue[:2])
                colourList.append(colourData[webSafe])
            else:
                image[i][j] = [0,0,0]
    colFreq = Counter(colourList)
    totalPixels = sum(list(colFreq.values()))
    colFreq = Counter(colourList).most_common(len(Counter(colourList)))
    for colour in colFreq:
        print(colour[0] + ": " + str(round(colour[1]/totalPixels*100,0)) +"%")
    imshow("image", image)
    imshow("edges", edges)
    


if __name__ == '__main__':
    detectColour("images/infuser1.jpg")
