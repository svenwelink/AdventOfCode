# Day 17 
print("Day 17")

import utils

test = utils.importData("2023/TestInput/day17.txt")
data = utils.importData("2023/Input/day17.txt")

def changeStringListToInterger(numberList):
    numberList = list(map(int, numberList))
    return(numberList)

def getFrame(data):
    dataList, ditsFrame = [], []
    for i in range(len(data)):
        rowList, distRow = [], []
        row = data[i].strip()
        for j in range(len(row)):
            rowList.append(int(row[j]))
            distRow.append(-1)
        dataList.append(rowList)
        ditsFrame.append(distRow)
    return(dataList, ditsFrame)

def runPartOne(data):
    dataFrame, distFrame = getFrame(data)
    directionFrame = distFrame.copy()
    startPos = [0, 0, "Left", 0]
    distFrame[0][0] = 0
    
    Hi = 3
    while distFrame[len(distFrame) - 1][len(distFrame[0])-1] == -1 and Hi < 10:
        
    return()

def getNextClosest(dataFrame, distFrame, directionFrame):

def getCornerPoints(distFrame):
    yMax, xMax = len(distFrame) - 1, len(distFrame[0]) - 1
    cornerPoints = []
    for i in range(len(yMax)):
        for j in range(len(xMax)):
            if distFrame[i][j] > 0:
                if i < yMax:
                    if distFrame[i][j+1] == -1:
                        cornerPoints.append([[i][j+1]])
                if i > 0:
                    if distFrame[i][j-1] == -1:
                        cornerPoints.append([[i][j-1]])
                if j < xMax:
                    if distFrame[i+1][j] == -1:
                        cornerPoints.append([[i+1][j]])
                if j > 0:
                    if distFrame[i-1][j] == -1:
                        cornerPoints.append([[i-1][j]])
    return(cornerPoints)


print(runPartOne(test))
