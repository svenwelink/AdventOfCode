import utils
import numpy as np
import matplotlib.path as mplPath
from operator import attrgetter

test = utils.importData("TestInput/day09.txt")
input = utils.importData("Input/day09.txt")

class coords:
    def __init__(self, string):
        splitString = string.split(",")
        self.x = int(splitString[0])
        self.y = int(splitString[1])
        self.sizePreviousAndNextPoint = 0

    def setSize(self, size):
        self.sizePreviousAndNextPoint = size

def calcSquareSize(p1:coords, p2:coords):
    lenght = abs(p1.x - p2.x) + 1
    height = abs(p1.y - p2.y) + 1
    return lenght * height

def runPartOne(data):
    highestValue = 0 
    allCoords = [coords(row) for row in data]

    for x in range(len(allCoords)):
        for y in range(x+1, len(allCoords)):
            size = calcSquareSize(allCoords[x], allCoords[y])
            if size > highestValue:
                highestValue = size
    return highestValue

print(runPartOne(input))

def getStartPoints(allCoords):
    for i in range(len(allCoords)):
        if i == 0:
            allCoords[i].setSize(calcSquareSize(allCoords[-1], allCoords[1]))
        elif i == (len(allCoords) - 1):
            allCoords[i].setSize(calcSquareSize(allCoords[i - 1] , allCoords[0]))
        else:
            allCoords[i].setSize(calcSquareSize(allCoords[i - 1], allCoords[i + 1]))

    startPointList = allCoords.copy()
    startPointList = sorted(startPointList, key=attrgetter('sizePreviousAndNextPoint'), reverse=True)
 
    return startPointList[0:2]

def prepDataForPolygon(data):
    newData = []
    for row in data:
        rowList = row.strip().split(",")
        newData.append([int(rowList[0]), int(rowList[1])])
    return newData

def squareCornersIsAllowed(p1:coords, p2:coords, polygon):
    sides = [[p1.x, p1.y], [p2.x, p2.y], [p1.x, p2.y], [p2.x, p1.y]]
    if allPointsAreInPolygon(sides, polygon):
                return True
    return False

def squareIsAllowed(p1:coords, p2:coords, polygon):
    sides = []
    for x in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
        sides.append([x, p1.y])
        sides.append([x, p2.y])
    for y in range(min(p1.y, p2.y) + 1, max(p1.y, p2.y)):
        sides.append([p1.x, y])
        sides.append([p2.x, y])
    if allPointsAreInPolygon(sides, polygon):
                return True
    return False

def allPointsAreInPolygon(sides, polygon):
    if all(polygon.contains_points(np.array(sides), radius = 0.001)):
        return True
    return False

def runPartTwo(data):
    polygon = mplPath.Path(np.array(prepDataForPolygon(data)))
    allCoords = [coords(row) for row in data]
    startPointList =  getStartPoints(allCoords)
    highestValue = 0

    for x in range(len(startPointList)):
        for y in range(0, len(allCoords)):
            size = calcSquareSize(startPointList[x], allCoords[y])
            if size > highestValue:
                if squareCornersIsAllowed(startPointList[x], allCoords[y], polygon):
                    if squareIsAllowed(startPointList[x], allCoords[y], polygon):
                        highestValue = size
    return highestValue

print(runPartTwo(input))
