import utils
from operator import attrgetter

test = utils.importData("TestInput/day09.txt")
input = utils.importData("Input/day09.txt")

class coords:
    def __init__(self, string):
        splitString = string.split(",")
        self.x = int(splitString[0])
        self.y = int(splitString[1])

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
