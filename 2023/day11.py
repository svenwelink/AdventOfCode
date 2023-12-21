# Day 11
print("Day 11")

import numpy as np
import utils

test = utils.importData("2023/TestInput/day11.txt")
data = utils.importData("2023/Input/day11.txt")

def runPartOne(data):
    extraRows, extraColumns = getRowsToDouble(data), getColumnsToDouble(data)
    galaxyList = getGalaxyList(data)
    distance = getGalaxyDistance(galaxyList, extraRows, extraColumns)
    return(distance)

def getRowsToDouble(data):
    rowsToAdd = []
    for i in range(len(data)):
        dataRow = data[i].strip()
        if len(set(dataRow)) == 1 and dataRow[0] == ".":
            rowsToAdd.append(int(i))

    return(rowsToAdd)

def turnDataIntoFrame(data):
    dataList = []
    for i in range(len(data)):
        rowList = []
        rowString = data[i].strip()
        for j in range(len(rowString)):
            rowList.append(rowString[j])
        dataList.append(rowList)
    return(dataList)

def getColumnsToDouble(data):
    dataFrame = turnDataIntoFrame(data)
    transposedData = np.array(dataFrame).T
    transposedDataList = transposedData.tolist()

    columnsToAdd = []
    for i in range(len(transposedDataList)):
        dataColumn = transposedDataList[i]
        if len(set(dataColumn)) == 1 and dataColumn[0] == ".":
            columnsToAdd.append(int(i))
    return(columnsToAdd)
    
def getGalaxyList(data):
    galaxyList = []

    for i in range(len(data)):
        row = data[i]
        for j in range(len(row)):
            if data[i][j] == "#":
                galaxyList.append([i, j])
    return(galaxyList)

def getGalaxyDistance(galaxyList, extraRows, extraColumns):
    totalDistance = 0

    for i in range(len(galaxyList)):
        for j in range(i + 1, len(galaxyList)):
            xMin, xMax = min(galaxyList[i][0], galaxyList[j][0]), max(galaxyList[i][0], galaxyList[j][0])
            yMin, yMax = min(galaxyList[i][1], galaxyList[j][1]), max(galaxyList[i][1], galaxyList[j][1])

            extraRowsBetween = len([x for x in extraRows if(x > xMin and x < xMax)])
            extraColumnsBetween  = len([x for x in extraColumns if(x > yMin and x < yMax)])

            distance = xMax - xMin + yMax - yMin + (extraRowsBetween + extraColumnsBetween)
            totalDistance += distance
    return(totalDistance)

print("Part 1")
testOne = runPartOne(test)
print("Test one:", testOne)
resultOne = runPartOne(data)
print("Result:", resultOne)


def runPartTwo(data):
    extraRows, extraColumns = getRowsToDouble(data), getColumnsToDouble(data)
    galaxyList = getGalaxyList(data)
    distance = getGalaxyDistanceTwo(galaxyList, extraRows, extraColumns)
    print(len(extraRows) + len(extraColumns))
    return(distance)

def getGalaxyDistanceTwo(galaxyList, extraRows, extraColumns):
    totalDistance = 0

    for i in range(len(galaxyList)):
        for j in range(i + 1, len(galaxyList)):
            xMin, xMax = min(galaxyList[i][0], galaxyList[j][0]), max(galaxyList[i][0], galaxyList[j][0])
            yMin, yMax = min(galaxyList[i][1], galaxyList[j][1]), max(galaxyList[i][1], galaxyList[j][1])

            extraRowsBetween = len([x for x in extraRows if(x > xMin and x < xMax)])
            extraColumnsBetween  = len([x for x in extraColumns if(x > yMin and x < yMax)])

            distance = xMax - xMin + yMax - yMin + (extraRowsBetween + extraColumnsBetween) * 999999
            totalDistance += distance

    return(totalDistance)

print("Part 2")
resultTwo = runPartTwo(data)
print("Result:", resultTwo)
