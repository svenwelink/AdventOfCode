import utils

test = utils.importData("TestInput/day03.txt")
input = utils.importData("Input/day03.txt")

def turnIntoList(value):
    return utils.changeStringListToInterger(value.strip())

def getValueOfRow(row):
    valueList = turnIntoList(row)
    firstNumber = max(valueList[:-1]) # get max value from list excl last value
    firstNumberIndex = valueList.index(firstNumber)
    secondNumber= max(valueList[(firstNumberIndex + 1):])
    return firstNumber * 10 + secondNumber

def runPartOne(data):
    totalSum = 0
    for row in data:
        totalSum += getValueOfRow(row)
    return totalSum

print(runPartOne(input))

def searchInList(valueList, numberToSearch, totalNumberString):
    lastFoundNumberIndex = valueList.index(numberToSearch)
    valueList[:lastFoundNumberIndex + 1] = [-1 for x in range(lastFoundNumberIndex)] # update list
    totalNumberString += str(numberToSearch)
    
    return lastFoundNumberIndex, valueList, totalNumberString

def getValueOfRowPartTwo(row):
    valueList = turnIntoList(row)
    lastFoundNumber = max(valueList[:-11]) # get max value from list excl last value
    lastFoundNumberIndex, valueList, totalNumberString = searchInList(valueList, lastFoundNumber, "")

    for x in range(11):
        # if the amount of charachters left is the amount that needs to be added
        if len(valueList[lastFoundNumberIndex:]) == (11 - x): 
            return int(totalNumberString + turnListIntoString(valueList[(lastFoundNumberIndex):]))
        
        else:
            lastFoundNumber = max(valueList[(lastFoundNumberIndex):(len(valueList) - 11 + x + 1)])
            lastFoundNumberIndex, valueList, totalNumberString = searchInList(valueList, lastFoundNumber, totalNumberString)
            
    return int(totalNumberString)

def turnListIntoString(xList):
    strElements = [str(element) for element in xList]
    stringToReturn = "".join(strElements)
    return stringToReturn

def runPartTwo(data):
    totalSum = 0
    for row in data:
        totalSum += getValueOfRowPartTwo(row)
    return totalSum

print(runPartTwo(input))
