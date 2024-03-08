# Day 12
print("Day 12")

import utils

test = utils.importData("TestInput/day12.txt")
data = utils.importData("Input/day12.txt")

def changeStringListToInterger(numberList):
    numberList = list(map(int, numberList))
    return(numberList)

def formatData(dataRow):
    row = dataRow.strip()
    field, numbers = row.split(" ")
    numbersListString = numbers.split(",")
    numbersList = changeStringListToInterger(numbersListString)
    return(field, numbersList)

def runPartOne(data):
    totalPossibilities = 0

    for i in range(len(data)):
        fieldString, numbers = formatData(data[i])
        allFieldStrings = getAllPosibleFieldStrings(fieldString)

        for string in allFieldStrings:
            if string.count("#") == sum(numbers): # Do not check de next line before beceaus it takes more time
                if getNumberListFromFieldString(string) == numbers:
                    totalPossibilities += 1

    return(totalPossibilities)

def getNumberListFromFieldString(fieldString):
    numberList = []
    number = 0
    for i in range(len(fieldString)):
        if fieldString[i] == "#":
            number += 1
        elif number > 0:
            numberList.append(number)
            number = 0
    if number > 0:
        numberList.append(number)
    return(numberList)

def getAllPosibleFieldStrings(fieldString):
    fieldStrings = []

def getAllPosibleFieldStrings(fieldString):
    fieldStringAsList = list(fieldString)
    fieldStrings = []
    countQuestionMark = fieldStringAsList.count("?")

    for x in range(2 ** countQuestionMark):
        copyString = fieldStringAsList.copy()
        binaryNumberString = str(bin(x))[2:]
        binaryNumberString = binaryNumberString.zfill(countQuestionMark)
        
        countQuestionMarksReplaced = 0
        for i in range(len(fieldStringAsList)):
            if copyString[i] == "?":
                if binaryNumberString[countQuestionMarksReplaced] == "0":
                    copyString[i] = "."
                else:
                    copyString[i] = "#"
                countQuestionMarksReplaced = countQuestionMarksReplaced + 1
            
        fieldStrings.append(copyString)

    return(fieldStrings)

print("Part one")
print("Test:", runPartOne(test))
print("Result:", runPartOne(data))

# Part 2 still needs work
