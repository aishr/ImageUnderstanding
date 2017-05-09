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
    isoImage = imread(imageName)
    origImage = imread(imageName)
    edges = Canny(origImage, 50, 150, 3)
    colourList = []
    allColours = []
    finalSelect = []
    backgroundColourSum = sum(origImage[0][0])

    for i in range(len(origImage)):
        for j in range(len(origImage[i])):
            numSum = sum(origImage[i][j])
            if numSum <= abs(backgroundColourSum - 60):
                hexValue = RGB2Hex(origImage[i][j])                
                webSafe = webSafeColour(hexValue[4:]) + webSafeColour(hexValue[2:4]) + webSafeColour(hexValue[:2])
                colourList.append(colourData[webSafe])
            else:
                isoImage[i][j] = [0,0,0]
    colFreq = Counter(colourList)
    totalPixels = sum(list(colFreq.values()))
    colFreq = colFreq.most_common(len(colFreq))
    print("All Colours Detected:")
    for i in range(len(colFreq)):
        percent = round(colFreq[i][1]/totalPixels*100,0)
        colFreq[i] += (percent,)
        if str(percent) != '0.0':
            print(colFreq[i][0] + ": " + str(percent) + "%")
            allColours.append([colFreq[i][0],percent])
    prevFreq = allColours[0][1]
    finalSelect.append(allColours[0][0])
    for i in range(1,len(allColours)):
        if prevFreq - allColours[i][1] <= 20.0 and allColours[i][1] >= 20.0:
            finalSelect.append(allColours[i][0])
        else:
            break;
        prevFreq = allColours[i][1]

    print("\n")
    print('Final Set of Colours (Total Count: ' + str(len(finalSelect)) + ')')
    for i in range(len(finalSelect)):
        print(str(i+1) + ") " + finalSelect[i])
    imshow("image", origImage)
    imshow("edges", edges)
    imshow("background", isoImage)
##    print(colFreq)
    return finalSelect
    
if __name__ == '__main__':
    detectColour("images/book4.jpg")
