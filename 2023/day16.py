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
    posToGetNextList, fullCircleList = [lastPos], []

    while len(posToGetNextList) > 0:
        lightFrame, posToGetNextList, fullCircleList = getNextPositions(lightFrame, posToGetNextList, fullCircleList, frame, bounds)

    return(lightFrame)

def getNextPositions(lightFrame, posToGetNextList, fullCircleList, frame, bounds):
    newPosToGetNextList = []
    
    for positionToCheck in posToGetNextList:
        if frame[positionToCheck[0]][positionToCheck[1]] == ".":
            newPosToGetNextList, lightFrame = moveToNextPosition(positionToCheck, newPosToGetNextList, lightFrame, bounds)
        elif frame[positionToCheck[0]][positionToCheck[1]] == "/":
            newPosToGetNextList, lightFrame = nextPosForwardSlash(positionToCheck, newPosToGetNextList, lightFrame, bounds)
        elif frame[positionToCheck[0]][positionToCheck[1]] == "\\":
            newPosToGetNextList, lightFrame = nextPosBackSlash(positionToCheck, newPosToGetNextList, lightFrame, bounds)
        elif frame[positionToCheck[0]][positionToCheck[1]] == "-":
            newPosToGetNextList, lightFrame, fullCircleList = nextPosVerticalSplitter(positionToCheck, newPosToGetNextList, lightFrame, bounds, fullCircleList)
        elif frame[positionToCheck[0]][positionToCheck[1]] == "|":    
            newPosToGetNextList, lightFrame, fullCircleList = nextPosHorizontalSplitter(positionToCheck, newPosToGetNextList, lightFrame, bounds, fullCircleList)

    return(lightFrame, newPosToGetNextList, fullCircleList)

def moveToNextPosition(currentPos, newPosToGetNextList, lightFrame, bounds):
    if currentPos[2] == "Down": 
        nextPos = [currentPos[0] + 1, currentPos[1], currentPos[2]]
    elif currentPos[2] == "Up": 
        nextPos = [currentPos[0] - 1, currentPos[1], currentPos[2]]
    elif currentPos[2] == "Left": 
        nextPos = [currentPos[0], currentPos[1] - 1, currentPos[2]]
    elif currentPos[2] == "Right": 
        nextPos = [currentPos[0], currentPos[1] + 1, currentPos[2]]

    if notInBounds(nextPos, bounds):
        newPosToGetNextList.append(nextPos)
        lightFrame[nextPos[0]][nextPos[1]] = 1

    return(newPosToGetNextList, lightFrame)

def nextPosForwardSlash(currentPos, newPosToGetNextList, lightFrame, bounds):
    # /
    if currentPos[2] == "Up":
        currentPos[2] = "Right"
    elif currentPos[2] == "Down":
        currentPos[2] = "Left"
    elif currentPos[2] == "Left":
        currentPos[2] = "Down"
    elif currentPos[2] == "Right":
        currentPos[2] = "Up"

    newPosToGetNextList, lightFrame = moveToNextPosition(currentPos, newPosToGetNextList, lightFrame, bounds)

    return(newPosToGetNextList, lightFrame)

def nextPosBackSlash(currentPos, newPosToGetNextList, lightFrame, bounds):
    # \
    if currentPos[2] == "Up":
        currentPos[2] = "Left"
    elif currentPos[2] == "Down":
        currentPos[2] = "Right"
    elif currentPos[2] == "Left":
        currentPos[2] = "Up"
    elif currentPos[2] == "Right":
        currentPos[2] = "Down"

    newPosToGetNextList, lightFrame = moveToNextPosition(currentPos, newPosToGetNextList, lightFrame, bounds)
        
    return(newPosToGetNextList, lightFrame)

def notInFullCirleList(pos, fullCircleList):
    if pos in fullCircleList:
        return(False)
    return(True)

def nextPosVerticalSplitter(currentPos, newPosToGetNextList, lightFrame, bounds, fullCircleList):
    # -
    if currentPos[2] == "Left" or currentPos[2] == "Right":
        newPosToGetNextList, lightFranextPosDotme = moveToNextPosition(currentPos, newPosToGetNextList, lightFrame, bounds)
    else:
        for i in range(-1, 2, 2):
            if i == -1:
                nextPos = [currentPos[0], currentPos[1] + i, "Left"]
            else:
                nextPos = [currentPos[0], currentPos[1] + i, "Right"]

            if notInBounds(nextPos, bounds) and notInFullCirleList(nextPos, fullCircleList):
                newPosToGetNextList.append(nextPos)
                fullCircleList.append(nextPos)
                lightFrame[nextPos[0]][nextPos[1]] = 1

    return(newPosToGetNextList, lightFrame, fullCircleList)

def nextPosHorizontalSplitter(currentPos, newPosToGetNextList, lightFrame, bounds, fullCircleList):
    # | 
    if currentPos[2] == "Up" or currentPos[2] == "Down":
        newPosToGetNextList, lightFrame = moveToNextPosition(currentPos, newPosToGetNextList, lightFrame, bounds)
    else: # Split horizontal
        for i in range(-1, 2, 2):
            if i == -1: 
                nextPos = [currentPos[0] + i, currentPos[1], "Up"]
            else:
                nextPos = [currentPos[0] + i, currentPos[1], "Down"]

            if notInBounds(nextPos, bounds) and notInFullCirleList(nextPos, fullCircleList):
                newPosToGetNextList.append(nextPos)
                fullCircleList.append(nextPos)
                lightFrame[nextPos[0]][nextPos[1]] = 1

    return(newPosToGetNextList, lightFrame, fullCircleList)

def notInBounds(positon, bounds):
    # Opschonen naar nieuwe techniek
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
        nextPos = [startPos[0] + 1, startPos[1], "Down"]
    elif startPos[0] == bounds[1][0]:
        nextPos = [startPos[0] - 1, startPos[1], "Up"]
    elif startPos[1] == bounds[0][1]:
        nextPos = [startPos[0], startPos[1] + 1, "Right"]
    elif startPos[1] == bounds[1][1]:
        nextPos = [startPos[0], startPos[1] - 1, "Left"]

    lightFrame[nextPos[0]][nextPos[1]] = 1
    return(nextPos, lightFrame)

def runPartOne(data, startPos = [0, -1]):
    dataFrame = utils.getRawFrame(data)
    lightFrame = runLigthTroughFrame(dataFrame, startPos)
    totalSum = 0
    
    for i in range(len(lightFrame)):
        totalSum += sum(lightFrame[i])

    return(totalSum)

print("Part 1")
print("Test:", runPartOne(test))
print("Result:", runPartOne(data))

def getStartPosList(data):
    dataFrame = utils.getRawFrame(data)
    bounds = getBounds(dataFrame)
    startPosList = []

    for i in range(0, bounds[1][0]):
        startPosList.append([-1,i])
        startPosList.append([bounds[1][0], i])

    for i in range(0, bounds[1][1]):
        startPosList.append([i,-1])
        startPosList.append([i, bounds[1][1]])
    return(startPosList)

def runPartTwo(data):
    startPosList = getStartPosList(data)
    bestRun = 0

    for pos in startPosList:
        runScore = runPartOne(data, pos)
        if runScore > bestRun:
            bestRun = runScore

    return(bestRun)

print("Part 2")
print("Test:", runPartTwo(test))
print("Result:", runPartTwo(data))
