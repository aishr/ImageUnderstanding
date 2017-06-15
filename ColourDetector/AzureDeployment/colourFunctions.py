from cv2 import *
from numpy import *
from collections import Counter
import urllib.request
import sys

class ColourFunctions():

    def __init__(dictFile):
        self.dictFile = dictFile

    def makeDictionary(self):
        fd = open(self.dictFile)
        lst = fd.readlines()
        dic = {}
        for i in range(len(lst)):
            lst[i] = lst[i].strip().split(",")
        for line in lst:
            dic[line[0]] = [line[1],line[2]]
            fd.close()
            return dic

    def RGB2Hex(self, rgb):
        hexNum = ''
        for num in rgb:
            if len(hex(num)) != 4:
                hexNum += "0"
            hexNum += hex(num)[2:]
        return hexNum

    def webSafeColour(self, num):
        num = int(num,16)
        num = 51 * ((num + 25)//51)
        num = hex(num)[2:]
        if len(num) != 2:
            num = '0' + num
        return num

    def URLToImage(self, url):
        resp = urllib.request.urlopen(url)
        image = asarray(bytearray(resp.read()), dtype="uint8")
        image = imdecode(image, IMREAD_COLOR)
        return image

    def detectColour(self, origImage):
        colourData = makeDictionary(self.dictFile)
        #origImage = imread(origImage)
        colourList = []
        #specColourList = []
        allColours = []
        #specColours = []
        finalSelect = []
        #finalSpecSelect = []
        backgroundColourSum = sum(origImage[0][0])

        for i in range(len(origImage)):
            for j in range(len(origImage[i])):
                numSum = sum(origImage[i][j])
                if numSum <= abs(backgroundColourSum - 60):
                    hexValue = self.RGB2Hex(origImage[i][j])                
                    webSafe = self.webSafeColour(hexValue[4:]) + self.webSafeColour(hexValue[2:4]) + self.webSafeColour(hexValue[:2])
                    colourList.append(colourData[webSafe][0])
                    #specColourList.append(colourData[webSafe][1])                
        colFreq = Counter(colourList)
        totalPixels = sum(list(colFreq.values()))
        colFreq = colFreq.most_common(len(colFreq))
        for i in range(len(colFreq)):
            percent = round(colFreq[i][1]/totalPixels*100,0)
            colFreq[i] += (percent,)
            if str(percent) != '0.0':
                allColours.append([colFreq[i][0],percent])
        
        if len(allColours) != 0:
            prevFreq = allColours[0][1]
            finalSelect.append([allColours[0][0],allColours[0][1]])
            for i in range(1,3):
                if i < len(allColours):
                    if allColours[i][1] >= 20.0 and prevFreq - allColours[i][1] <= 20.0:
                        finalSelect.append([allColours[i][0],allColours[i][1]])
                    else:
                        break;
                    prevFreq = allColours[i][1]
        else: # Should Never Reach Here
            finalSelect.append("nothing")

        return finalSelect
