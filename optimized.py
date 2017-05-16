'''
Colour Detector for General Merchandising Products

Algorithm
1) Detect background colour
2) Ignore background
3) Record all pixel colours based on Web Safe Colours
4) Find most common colours
5) Calculate percentages of each colour in the item
6) Generalize to maximum 3 colours

Edge Cases
1) Items with other content (infuser)
2) Items who's colour is not the bulk of the item (mirror)
3) Metallic Gold & Copper (will detect as yellow or brown respectively)
4)

Good Examples
1) Red and pink wine glass: 657284666103: SLANT COLLECTIONS STEMLESS WINE GLASS – SINGLE BELLS
2) purple yellow backpack: 732396464226: Backpack - Butterfly 3-8 yrs by Crocodile Creek
3) green rustic mug:
4) retro phone yellow:
5) blue digi dino:
6) bashful dino
'''
from cv2 import *
from numpy import *
from collections import Counter
import urllib.request
import sys

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

def URLToImage(url):
    resp = urllib.request.urlopen(url)
    image = asarray(bytearray(resp.read()), dtype="uint8")
    image = imdecode(image, IMREAD_COLOR)
    return image

def detectColour(imageName):
    colourData = makeDictionary()
    origImage = imread(imageName)
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
##            else:
##                isoImage[i][j] = [0,0,0]
    colFreq = Counter(colourList)
    print(colFreq)
    print('\n')
    totalPixels = sum(list(colFreq.values()))
    print("Total Pixels Counted: " + str(totalPixels))
    print("\n")
    colFreq = colFreq.most_common(len(colFreq))
    print("All Colours Detected:")
    for i in range(len(colFreq)):
        percent = round(colFreq[i][1]/totalPixels*100,0)
        colFreq[i] += (percent,)
        if str(percent) != '0.0':
            print(colFreq[i][0] + ": " + str(percent) + "%")
            allColours.append([colFreq[i][0],percent])
    if len(allColours) != 0:
        prevFreq = allColours[0][1]
        finalSelect.append([allColours[0][0],allColours[0][1]])
        for i in range(1,3):
            if i < len(allColours):
                if prevFreq - allColours[i][1] <= 20.0: # or prevFreq - allColours[i][1] <= 20.0:
                    finalSelect.append([allColours[i][0],allColours[i][1]])
                else:
                    break;
                prevFreq = allColours[i][1]
    else: # Should Never Reach Here
        finalSelect.append("nothing")

    print("\n")
    print('Final Set of Colours (Total Count: ' + str(len(finalSelect)) + ')')
    for i in range(len(finalSelect)):
        print(str(i+1) + ") " + finalSelect[i][0] + " at " + str(finalSelect[i][1]) + "%")
    imshow("image", origImage)
##    imshow("edges", edges)
##    imshow("background", isoImage)
##    print(colFreq)
    print(finalSelect)
    return finalSelect

def storeColours(readFile, writeFile=None):
    fdr = open(readFile, 'r')
    file = fdr.readlines()
    fdr.close()
    if writeFile:
        fdw = open(writeFile, 'w')
    else:
        fdw = sys.stdout

    fdw.write("SKU,Name,Image,colour1,percent1,colour2,percent2,colour3,percent3\n")
    for i in range(len(file)):
        file[i] = file[i].strip().split(',')
        url = file[i][2]
        image = URLToImage(url)
        colours = detectColour(image)
        
        fdw.write(file[i][0]+','+file[i][1]+',"'+file[i][2]+'",')
        for j in range(len(colours)):
            if j != (len(colours) - 1):
                fdw.write(colours[j][0] + "," + str(colours[j][1])+",")
            else:
                fdw.write(colours[j][0] + "," + str(colours[j][1])+"\n")
        print(str(i+1))

    fdw.close()
        
    
    
if __name__ == '__main__':
    detectColour("images/backpack1.jpg")
    #storeColours("testfile.csv","colGM.csv")
