import utils

test = utils.importData("TestInput/day02.txt")[0].split(",")
input = utils.importData("Input/day02.txt")[0].split(",")
    
def isValidXTimes(idString, x):
    if len(idString) % x == 0 and len(idString) >= x:
        lengthSlices = int(len(idString) / x)
        for i in range(x - 1):
            if idString[int(i * lengthSlices):int((i + 1) * lengthSlices)] != idString[int((i + 1) * lengthSlices):int((i + 2) * lengthSlices)]:
                return False

        return True
    return False

def totalValueForRange(rangeString):
    totalValue = 0
    idRange = rangeString.split("-")
    for id in range(int(idRange[0]), int(idRange[1]) + 1):
        stringId = str(id)
        if isValidXTimes(stringId, 2):
            totalValue += id
    return totalValue

def runPartOne(data):
    totalSum = 0
    for instruction in data:
        totalSum += totalValueForRange(instruction)
    return(totalSum)

print(runPartOne(input))

def isValidPartTwo(idString):
    xTimesToCheck = [2, 3, 5, 7]
    for x in xTimesToCheck:
        if isValidXTimes(idString, x):
            return True
    return False

def totalValueForRangePartTwo(rangeString):
    totalValue = 0
    idRange = rangeString.split("-")
    for id in range(int(idRange[0]), int(idRange[1]) + 1):
        stringId = str(id)
        if isValidPartTwo(stringId):
            totalValue += id

    return totalValue

def runPartTwo(data):
    totalSum = 0
    for instruction in data:
        totalSum += totalValueForRangePartTwo(instruction)
    return(totalSum)

print(runPartTwo(input))
