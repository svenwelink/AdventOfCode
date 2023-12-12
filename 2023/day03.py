# Day 3
print("Day 3")
# Import data
def importData(path):
    file = open(pathFile,'r')
    data = file.readlines()
    file.close()
    return(data)

pathFile = # path
data = importData(pathFile)

nRows, nCols = len(data), len(data[0]) - 1

# Part 1
print("Part 1")

def runPartOne():
    totalSum = 0

    for rowId in range(nRows):
        numberLengthCount = 0

        for colId in range(nCols):
            if data[rowId][colId].isnumeric():
                numberLengthCount += 1 
            
            # If not numeric, check numberLengthCount
            elif numberLengthCount > 0:
                if checkForSignAroundNumber(rowId, colId, numberLengthCount):
                    totalSum += int(data[rowId][(colId - numberLengthCount):(colId)])

                numberLengthCount = 0
            

        # Check if the last few characters where numbers    
        if numberLengthCount > 0:
            # Check the number for signs 
            if checkForSignAroundNumber(rowId, (nCols - 1), numberLengthCount):
                totalSum += int(data[rowId][(nCols -  numberLengthCount):nCols + 1])   

    return(totalSum)

def checkForSignAroundNumber(rowId, colId, lengthOfNumber):
    for checkRowId in range(max(0, rowId - 1), (min(nRows - 1, rowId + 1)) + 1):

        for checkColId in range(max(0, (colId - lengthOfNumber - 1)), min(nCols, (colId + 1))):
            dataPoint = data[checkRowId][checkColId]

            if dataPoint.isnumeric() == False and dataPoint != ".":
                return(True)

    return(False)

print(runPartOne())

# Part 2
print("part 2")

def runPartTwo():
    totalGearSum = 0

    for rowId in range(nRows):
        for colId in range(nCols):
            
            if data[rowId][colId] == "*":
                gearNumberList = getGearNumbers(rowId, colId)

                if len(gearNumberList) == 2:
                    totalGearSum += int(gearNumberList[0]) * int(gearNumberList[1])

    return(totalGearSum)

def getGearNumbers(rowId, colId):
    numberList = []
    numberCordinatesList = []

    for checkRowId in range(max(0, rowId - 1), (min(nRows - 1, rowId + 1)) + 1):

        for checkColId in range(max(0, (colId - 1)), min(nCols, (colId + 2))):
            dataPoint = data[checkRowId][checkColId]

            if dataPoint.isnumeric():
                number, numberCordinates = getNumber(checkRowId, checkColId)

                if numberCordinates not in numberCordinatesList:
                    numberList.append(number)
                    numberCordinatesList.append(numberCordinates)

    return(numberList)

def getNumber(rowId, colId):
    row = data[rowId]
    startNumberColId, endNumberColId = colId, colId

    while row[startNumberColId].isnumeric():
        startNumberColId -= 1

    while row[endNumberColId].isnumeric():
        endNumberColId += 1

    startNumberColId = max(0, (startNumberColId + 1))
    endNumberColId = min(endNumberColId, (nCols))

    number = int(row[startNumberColId:endNumberColId])
    return(number, [rowId, startNumberColId, endNumberColId])

print(runPartTwo())
