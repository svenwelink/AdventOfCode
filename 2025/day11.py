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
    def __init__(self, pathList):
        self.list = pathList

    def lastNode(self):
        return self.list[-1]
    
    def addPoint(self, point):
        self.list.append(point)

    def containsNoLoop(self):
        if len(self.list) == len(list(set(self.list))):
            return True
        return False


def calculatePathsBetweenTwoPoints(data, inString = "you", outString = "out"):
    pathsToCheck, totalPaths, roundCount= [path([inString])], 0, 0
    while len(pathsToCheck) > 0 and roundCount < len(data):
        print("Round: ", str(roundCount), " Paths to check: ", str(len(pathsToCheck)))
        newPaths = []

        for pathToCheck in pathsToCheck:
            newPoints = [x.newPoints for x in data if x.name == pathToCheck.lastNode()][0]
            
            for point in newPoints:
                newPath = path(pathToCheck.list.copy())
                
                if point != outString and point != "out":
                    newPath.addPoint(point)
                    if newPath.containsNoLoop():
                        newPaths.append(newPath)
                elif point == outString:
                    totalPaths += 1

        pathsToCheck = newPaths
        roundCount += 1
    return totalPaths

def runPartTwo(data):
    toSplitPoint = prepData(data)

    dacToOut = calculatePathsBetweenTwoPoints(toSplitPoint, "dac", "out")
    #fftToOut = calculatePathsBetweenTwoPoints(toSplitPoint, "fft", "out")
    #dacToFft = calculatePathsBetweenTwoPoints(toSplitPoint, "dac", "fft")
    fftToDac = calculatePathsBetweenTwoPoints(toSplitPoint, "fft", "dac")
    #svrToDac = calculatePathsBetweenTwoPoints(toSplitPoint, "svr", "dac")
    svrToFft = calculatePathsBetweenTwoPoints(toSplitPoint, "svr", "fft")

    svrToOut = svrToFft * fftToDac * dacToOut #+ svrToDac * dacToFft * fftToOut
    return svrToOut

print(runPartTwo(input))
