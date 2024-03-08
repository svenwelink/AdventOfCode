import utils

test = utils.importData("TestInput/day09.txt")
data = utils.importData("Input/day09.txt")

def getNextNumberList(inputList):
    if len(set(inputList)) == 1:
        return(inputList[-1])
    else:
        newList = []
        for i in range(len(inputList) - 1):
            numberInList = inputList[i+1] - inputList[i]
            newList.append(numberInList)
        
    listUnderLastNumber = getNextNumberList(newList)
    return(inputList[-1] + listUnderLastNumber)

def getListFromString(string):
    numberList = string.split(" ")
    numberList = list(map(int, numberList))
    return(numberList)

def getNextNumberLine(line):
    numberList = getListFromString(line)
    nextNumber = getNextNumberList(numberList)
    return(nextNumber)

def runPartOne(data):
    totalPoints = 0
    for i in range(len(data)): 
        pointsRow = getNextNumberLine(data[i])
        totalPoints += pointsRow

    return(totalPoints)

print("Day 9")
print("Part one")

testOne = runPartOne(test)
print("Test result:", testOne)
resultOne = runPartOne(data)
print("Result:", resultOne)

def getNextNumberLinePartTwo(line):
    numberList = getListFromString(line)
    nextNumber = getNextNumberListPartTwo(numberList)
    return(nextNumber)

def getNextNumberListPartTwo(inputList):
    if len(set(inputList)) == 1:
        return(inputList[0])
    else:
        newList = []
        for i in range(len(inputList) - 1):
            numberInList = inputList[i+1] - inputList[i]
            newList.append(numberInList)

    listUnderFirstNumber = getNextNumberListPartTwo(newList)
    return (inputList[0] - listUnderFirstNumber)

def runPartTwo(data):
    totalPoints = 0
    for i in range(len(data)): 
        pointsRow = getNextNumberLinePartTwo(data[i])
        totalPoints += pointsRow

    return(totalPoints)

print("Part two")
testTwo = runPartTwo(test)
print("Test result:", testTwo)
resultTwo = runPartTwo(data)
print("Result:", resultTwo)
