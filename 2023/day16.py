# Day 16
print("Day 16")

import utils

test = utils.importData("2023/TestInput/day16.txt")
data = utils.importData("2023/Input/day16.txt")

def getLightFrame(dataFrame):
    newFrame = []
    for i in range(len(dataFrame)):
        rowFrame = []
        for j in range(len(dataFrame[i])):
            rowFrame.append(0)
        newFrame.append(rowFrame)
    return(newFrame)

def runLigthTroughFrame(frame, lastPosMinusOne):
    lightFrame, bounds = getLightFrame(frame), getBounds(frame)
    lastPos, lightFrame = getFirstNextPos(lastPosMinusOne, bounds, lightFrame)
    posToGetNextList, fullCircleList = [[lastPosMinusOne, lastPos]], []

    while len(posToGetNextList) > 0:
        lightFrame, posToGetNextList, fullCircleList = getNextPositions(lightFrame, posToGetNextList, fullCircleList, frame, bounds)
        
        # for i in range(len(lightFrame)):
        #     print(lightFrame[i])
        # print("")
        # test = input(" Press enter")
    return(lightFrame)

def getNextPositions(lightFrame, posToGetNextList, fullCircleList, frame, bounds):
    newPosToGetNextList = []
    
    for positionToCheck in posToGetNextList:
        lastPos, currentPos = positionToCheck[0], positionToCheck[1]
        if frame[currentPos[0]][currentPos[1]] == ".":
            newPosToGetNextList, lightFrame = nextPosDot(lastPos, currentPos, newPosToGetNextList, lightFrame, bounds)
        elif frame[currentPos[0]][currentPos[1]] == "/":
            newPosToGetNextList, lightFrame = nextPosForwardSlash(lastPos, currentPos, newPosToGetNextList, lightFrame, bounds)
        elif frame[currentPos[0]][currentPos[1]] == "\\":
            newPosToGetNextList, lightFrame = nextPosBackSlash(lastPos, currentPos, newPosToGetNextList, lightFrame, bounds)
        elif frame[currentPos[0]][currentPos[1]] == "-":
            newPosToGetNextList, lightFrame, fullCircleList = nextPosVerticalSplitter(lastPos, currentPos, newPosToGetNextList, lightFrame, bounds, fullCircleList)
        elif frame[currentPos[0]][currentPos[1]] == "|":    
            newPosToGetNextList, lightFrame, fullCircleList = nextPosHorizontalSplitter(lastPos, currentPos, newPosToGetNextList, lightFrame, bounds, fullCircleList)

    return(lightFrame, newPosToGetNextList, fullCircleList)

def nextPosDot(lastPos, currentPos, newPosToGetNextList, lightFrame, bounds):
    # If x-axis is the same
    if currentPos[0] == lastPos[0]:
        nextPos = [currentPos[0], currentPos[1] + currentPos[1] - lastPos[1]]
    # Else y-axis is the same
    else:
        nextPos = [currentPos[0] + currentPos[0] - lastPos[0], currentPos[1]]
            
    if notInBounds(nextPos, bounds):
        newPosToGetNextList.append([currentPos, nextPos])
        lightFrame[nextPos[0]][nextPos[1]] = 1

    return(newPosToGetNextList, lightFrame)

def nextPosForwardSlash(lastPos, currentPos, newPosToGetNextList, lightFrame, bounds):
    # /
    # If x-axis is the same 
    if currentPos[0] == lastPos[0]:
        if currentPos[1] > lastPos[1]: # From left
            nextPos = [currentPos[0] - 1, currentPos[1]]
        else: # From right
            nextPos = [currentPos[0] + 1, currentPos[1]]
    # Else y-axis is the same
    else:
        if currentPos[0] > lastPos[0]: # From above
            nextPos = [currentPos[0], currentPos[1] - 1]
        else: # From below
            nextPos = [currentPos[0], currentPos[1] + 1]
            
    if notInBounds(nextPos, bounds):
        newPosToGetNextList.append([currentPos, nextPos])
        lightFrame[nextPos[0]][nextPos[1]] = 1

    return(newPosToGetNextList, lightFrame)

def nextPosBackSlash(lastPos, currentPos, newPosToGetNextList, lightFrame, bounds):
    # \
    # If x-axis is the same 
    if currentPos[0] == lastPos[0]:
        if currentPos[1] > lastPos[1]: # From left
            nextPos = [currentPos[0] + 1, currentPos[1]]
        else: # From right
            nextPos = [currentPos[0] - 1, currentPos[1]]
    # Else y-axis is the same
    else:
        if currentPos[0] > lastPos[0]: # From above
            nextPos = [currentPos[0], currentPos[1] + 1]
        else: # From below
            nextPos = [currentPos[0], currentPos[1] - 1]
            
    if notInBounds(nextPos, bounds):
        newPosToGetNextList.append([currentPos, nextPos])
        lightFrame[nextPos[0]][nextPos[1]] = 1
        
    return(newPosToGetNextList, lightFrame)

def notInFullCirleList(pos, fullCircleList):
    if pos in fullCircleList:
        return(False)
    return(True)

def nextPosVerticalSplitter(lastPos, currentPos, newPosToGetNextList, lightFrame, bounds, fullCircleList):
    # -
    if lastPos[0] == currentPos[0]: # Not the rightsplitter, so look at it as a dot
        newPosToGetNextList, lightFrame = nextPosDot(lastPos, currentPos, newPosToGetNextList, lightFrame, bounds)
    else: # Split vertical
        for i in range(-1, 2, 2):
            nextPos = [currentPos[0], currentPos[1] + i]
            if notInBounds(nextPos, bounds) and notInFullCirleList(nextPos, fullCircleList):
                newPosToGetNextList.append([currentPos, nextPos])
                fullCircleList.append(nextPos)
                lightFrame[nextPos[0]][nextPos[1]] = 1

    return(newPosToGetNextList, lightFrame, fullCircleList)

def nextPosHorizontalSplitter(lastPos, currentPos, newPosToGetNextList, lightFrame, bounds, fullCircleList):
    # | 
    if lastPos[1] == currentPos[1]: # Not the rightsplitter, so look at it as a dot
        newPosToGetNextList, lightFrame = nextPosDot(lastPos, currentPos, newPosToGetNextList, lightFrame, bounds)
    else: # Split horizontal
        for i in range(-1, 2, 2):
            nextPos = [currentPos[0] + i, currentPos[1]]
            if notInBounds(nextPos, bounds) and notInFullCirleList(nextPos, fullCircleList):
                newPosToGetNextList.append([currentPos, nextPos])
                fullCircleList.append(nextPos)
                lightFrame[nextPos[0]][nextPos[1]] = 1

    return(newPosToGetNextList, lightFrame, fullCircleList)

def notInBounds(positon, bounds):
    # Out of bounds x-axis
    if positon[0] == bounds[0][0] or positon[1] == bounds[0][1]:
        return(False)
    # Out of bounds y-axis
    elif positon[0] == bounds[1][0] or positon[1] == bounds[1][1]:
        return(False)
    return(True)

def getBounds(frame):
    minX, minY, maxX, maxY = -1, -1, len(frame), len(frame[0])
    bounds = [[minX, minY], [maxX, maxY]]
    return(bounds)

def getFirstNextPos(startPos, bounds, lightFrame):
    if startPos[0] == bounds[0][0]:
        nextPos = [startPos[0] + 1, startPos[1]]
    elif startPos[0] == bounds[1][0]:
        nextPos = [startPos[0] - 1, startPos[1]]
    elif startPos[1] == bounds[0][1]:
        nextPos = [startPos[0], startPos[1] + 1]
    elif startPos[1] == bounds[1][1]:
        nextPos = [startPos[0], startPos[1] - 1]

    lightFrame[nextPos[0]][nextPos[1]] = 1
    return(nextPos, lightFrame)

def runPartOne(data):
    dataFrame = utils.getRawFrame(data)
    lightFrame = runLigthTroughFrame(dataFrame, [0, -1])
    totalSum = 0
    
    for i in range(len(lightFrame)):
        totalSum += sum(lightFrame[i])

    return(totalSum)

print("Part 1")
print("Test:", runPartOne(test))
print("Result:", runPartOne(data))
