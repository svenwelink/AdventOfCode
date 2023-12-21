# Day 16
print("Day 16")

import utils

test = utils.importData("2023/TestInput/day16.txt")
data = utils.importData("2023/Input/day16.txt")

def getFrame(data):
    frame = []
    for i in range(len(data)):
        rowFrame = []
        row = r"{}".format(data[i]).strip()

        for j in range(len(row)):
            if len(row[j]) > 0:
                rowFrame.append(row[j])

        frame.append(rowFrame)

    return(frame)

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
    lastPos = getFirstNextPos(lastPosMinusOne, bounds)
    lightFrame[lastPos[0]][lastPos[1]] = 1

    
    return(lightFrame)

def getBounds(frame):
    minX, minY, maxX, maxY = -1, -1, len(frame), len(frame[0])
    bounds = [[minX, minY], [maxX, maxY]]
    return(bounds)

def getFirstNextPos(startPos, bounds):
    if startPos[0] == bounds[0][0]:
        nextPos = [startPos[0] + 1, startPos[1]]
    elif startPos[0] == bounds[1][0]:
        nextPos = [startPos[0] - 1, startPos[1]]
    elif startPos[1] == bounds[0][1]:
        nextPos = [startPos[0], startPos[1] + 1]
    elif startPos[1] == bounds[1][1]:
        nextPos = [startPos[0], startPos[1] - 1]
    return(nextPos)

def runPartOne(data):
    dataFrame = getFrame(data)
    ligthFrame = runLigthTroughFrame(dataFrame, [0, -1])
    return(ligthFrame)

print(runPartOne(test))
