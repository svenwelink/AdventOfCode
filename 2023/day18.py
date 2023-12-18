# Dy 18
print("Day 18")

def importData(path):
    file = open(path,'r')
    data = file.readlines()
    file.close()
    return(data)

pathFileData = # path
pathFileTestData = # path
data = importData(pathFileData)
test = importData(pathFileTestData)

def getLists(data):
    dataList = []
    for rowId in range(len(data)):
        rowStripped = data[rowId].strip()
        rowSplit = rowStripped.split(" ")
        dataList.append(rowSplit)
    return(dataList)

def getAllCorners(instructions):
    allCorners = [[0, 0]]
    for i in range(len(instructions)):
        newCorner = allCorners[i].copy()

        if instructions[i][0] == "R":
            newCorner[1] = newCorner[1] + int(instructions[i][1]) 
        elif instructions[i][0] == "L":
            newCorner[1] = newCorner[1] - int(instructions[i][1]) 
        elif instructions[i][0] == "D":
            newCorner[0] = newCorner[0] + int(instructions[i][1]) 
        elif instructions[i][0] == "U":
            newCorner[0] = newCorner[0] - int(instructions[i][1])

        allCorners.append(newCorner)
    return(allCorners)

def shoeLaceFormula(hookpoints):
    determinantSum = 0
    for i in range(len(hookpoints)):
        determinantSum += getDeterminant(hookpoints[i-1], hookpoints[i])
    area = abs(determinantSum/2)
    return(area)

def getDeterminant(pointOne, pointTwo):
    determinant = pointOne[0] * pointTwo[1] - pointOne[1] * pointTwo[0]
    return(determinant)

def getLength(instructions):
    totalLength = 0
    for i in range(len(instructions)):
        totalLength += int(instructions[i][1]) 
    return(totalLength)

def getInnerArea(area, length):
    innerArea = int((area - (length / 2)) + 1)
    return(innerArea)

def runPartOne(data):
    dataList = getLists(data)
    allCorners = getAllCorners(dataList)
    area, length = shoeLaceFormula(allCorners), getLength(dataList)
    innerArea = getInnerArea(area, length)

    totalArea = length + innerArea
    return(totalArea)

print("Part 1")
print("Test:", runPartOne(test))
print("Result:", runPartOne(data))

# Part Two
def getListsPartTwo(data):
    dataList = []
    for rowId in range(len(data)):
        rowStripped = data[rowId].strip()
        rowSplit = rowStripped.split(" ")
        hexaCode = rowSplit[2]

        distance = int(hexaCode[2:7],16)
        if int(hexaCode[7]) == 0:
            direction = "R"
        elif int(hexaCode[7]) == 1:
            direction = "D"
        elif int(hexaCode[7]) == 2:
            direction = "L"
        else:
            direction = "U" 

        dataList.append([direction, distance])
    return(dataList)

def runPartTwo(data):
    dataList = getListsPartTwo(data)
    allCorners = getAllCorners(dataList)
    area, length = shoeLaceFormula(allCorners), getLength(dataList)
    innerArea = getInnerArea(area, length)

    totalArea = length + innerArea
    return(totalArea)

print("Part 2")
print("Test:", runPartTwo(test))
print("Result:", runPartTwo(data))
