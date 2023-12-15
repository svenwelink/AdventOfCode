# Day 15
print("Day 15")

# Import data
def importData(path):
    file = open(path,'r')
    data = file.readlines()
    file.close()
    return(data)

pathFileData = # Path
pathFileTestData = # Path
data = importData(pathFileData)
test = importData(pathFileTestData)

def makeList(data):
    dataList = data[0].split(",")
    return(dataList)

def calculateNextValue(currentValue, character):
    valueChar = ord(character)
    currentValue += valueChar
    currentValue = currentValue * 17
    currentValue = currentValue % 256
    return(currentValue)

def runPartOne(data):
    totalSum = 0
    data = makeList(data)
    for string in data:
        currentValue = 0
        for charId in range(len(string)):
            currentValue = calculateNextValue(currentValue, string[charId])
        totalSum += currentValue

    return(totalSum)

print("Part 1")
print("Test:", runPartOne(test))
print("Result:", runPartOne(data))

# Part 2

def makeEmptyList(length = 256):
    emptyList = []
    for i in range(length):
        emptyList.append([])
    return(emptyList)

def removeFromBox(boxes, lensNames, currentValue, string, charId):
    boxNumber = currentValue

    if string[:charId] in lensNames[boxNumber]:
        placeInBox = lensNames[boxNumber].index(string[:charId])
        del boxes[boxNumber][placeInBox]
        del lensNames[boxNumber][placeInBox]

    return(boxes, lensNames)

def addLensToBox(boxes, lensNames, currentValue, string, charId):
    boxNumber = currentValue

    if string[:charId] in lensNames[boxNumber]:
        placeInBox = lensNames[boxNumber].index(string[:charId])
        boxes[boxNumber][placeInBox] = int(string[charId + 1])
        lensNames[boxNumber][placeInBox] = string[:charId]         
    else:
        boxes[boxNumber].append(int(string[charId + 1]))
        lensNames[boxNumber].append(string[:charId])

    return(boxes, lensNames)


def getAllBoxesWithLens(data):
    data = makeList(data)

    boxes, lensNames = makeEmptyList(), makeEmptyList()
    for string in data:
        currentValue, boxNumber = 0, -1

        for charId in range(len(string)):
            if string[charId] == "-":
                boxes, lensNames = removeFromBox(boxes, lensNames, currentValue, string, charId)

            elif string[charId] == "=":
                boxes, lensNames = addLensToBox(boxes, lensNames, currentValue, string, charId)

            elif boxNumber == -1:
                currentValue = calculateNextValue(currentValue, string[charId])
        
    return(boxes)

def runPartTwo(data):
    boxes = getAllBoxesWithLens(data)
    totalSum = 0
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):  
            valueRow = (j+1) * int(boxes[i][j]) * (i+ 1)
            totalSum += valueRow

    return(totalSum)

print("Part 2")
print("Test:", runPartTwo(test))
print("Result:", runPartTwo(data))
