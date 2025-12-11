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
    print(pointsToCheck)
    while len(pointsToCheck) > 0:
        pointsAfterSplits = []
        for pointName in pointsToCheck:
            point = [x for x in toSplitPoint if x.name == pointName][0]
            totalPaths += len(point.newPoints) - 1
            for x in point.newPoints:
                if x != outString and x != "out" and x != inString:
                    pointsAfterSplits.append(x) 

        pointsToCheck = pointsAfterSplits
    return totalPaths

print(runPartOne(input))

def runPartTwo(data):
    dacToOut = runPartOne(data, "dac", "out")
    fftToOut = runPartOne(data, "fft", "out")
    dacToFft = runPartOne(data, "dac", "fft")
    fftToDac = runPartOne(data, "fft", "dac")
    svrToDac = runPartOne(data, "svr", "dac")
    svrToFft = runPartOne(data, "svr", "fft")

    svrToOut = svrToFft * fftToDac * dacToOut + svrToDac * dacToFft * fftToOut
    return svrToOut

print(runPartTwo(test))
