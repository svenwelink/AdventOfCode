import utils

test = [x.strip() for x in utils.importData("TestInput/day11_2.txt")]
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

def runPartOne(data, inString = "you", outString = "out"):
    toSplitPoint = prepData(data)
    pointsToCheck, totalPaths = [inString], 1
    while len(pointsToCheck) > 0:
        pointsAfterSplits = []
        for pointName in pointsToCheck:
            point = [x for x in toSplitPoint if x.name == pointName][0]
            totalPaths += len(point.newPoints) - 1
            for x in point.newPoints:
                if x != outString:
                    pointsAfterSplits.append(x) 

        pointsToCheck = pointsAfterSplits
    return totalPaths

print(runPartOne(input))

class path:
    def __init__(self, name, pathCount):
        self.name = name
        self.pathCount = pathCount
    
    def addExtraPoints(self, count):
        self.pathCount += count

def calculatePathsBetweenTwoPoints(data, inString = "you", outString = "out"):
    pathsToCheck, totalPaths, roundCount = [path(inString, 1)], 0, 0
    while len(pathsToCheck) > 0:
        newPaths = []
        for pathToCheck in pathsToCheck:
            newPoints = [x.newPoints for x in data if x.name == pathToCheck.name][0]
        
            for pointName in newPoints:
                if pointName == outString:
                    totalPaths += pathToCheck.pathCount

                elif pointName == "out":
                    pass

                elif pointName != outString:
                    if pointName in [x.name for x in newPaths]:
                        index = [x.name for x in newPaths].index(pointName)
                        newPaths[index].addExtraPoints(pathToCheck.pathCount)
                    else:
                        newPaths.append(path(pointName, pathToCheck.pathCount))

        pathsToCheck = newPaths
        roundCount += 1
    
    return totalPaths

def runPartTwo(data):
    toSplitPoint = prepData(data)

    dacToOut = calculatePathsBetweenTwoPoints(toSplitPoint, "dac", "out")
    fftToDac = calculatePathsBetweenTwoPoints(toSplitPoint, "fft", "dac")
    svrToFft = calculatePathsBetweenTwoPoints(toSplitPoint, "svr", "fft")

    svrToOut = svrToFft * fftToDac * dacToOut
    return svrToOut

print(runPartTwo(input))
