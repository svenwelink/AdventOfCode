import utils

test = [x.strip() for x in utils.importData("TestInput/day11.txt")]
input = [x.strip() for x in utils.importData("Input/day11.txt")]

class toSplitPoint:
    def __init__(self, id, values):
        self.id = int(id)
        self.name = values[0]
        self.newPoints = values[1].strip().split(" ")
        self.splitIds = []

def prepData(data):
    splitedList = [x.split(":") for x in data]
    objectList = [toSplitPoint(id, splitedList[id]) for id in range(len(splitedList))]
    return objectList

def runPartOne(data):
    toSplitPoint = prepData(data)
    pointsToCheck, totalPaths = ["you"], 1
    while len(pointsToCheck) > 0:
        pointsAfterSplits = []
        for pointName in pointsToCheck:
            point = [x for x in toSplitPoint if x.name == pointName][0]
            totalPaths += len(point.newPoints) - 1
            for x in point.newPoints:
                if x != "out":
                    pointsAfterSplits.append(x) 

        pointsToCheck = pointsAfterSplits
    return totalPaths

print(runPartOne(input))
