# Day 1
import utils

test = utils.importData("2023/TestInput/day01.txt")
data = utils.importData("2023/Input/day01.txt")

def getFirstNumber(string):
    for i in range(0, len(string)):
        if string[i].isnumeric():
            return(int(string[i]))

def getSecondNumber(string):
    for i in range(len(string) - 1, -1, -1):
        if string[i].isnumeric():
            return(int(string[i]))
        
def runPart1(data):
    totalSum = int(0)
    for lineIndex in range(0, len(data)):
        line = data[lineIndex]
        totalSum += (getFirstNumber(line) * 10) + getSecondNumber(line)
    return(totalSum)

# Execute
print("Part 1")
print("Test:", runPart1(test))
print("Data:", runPart1(data))

# Part 2
# Functions
numbersText = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def getFirstNumberPart2(string):
    for i in range(0, len(string)):
        if string[i].isnumeric():
            return(int(string[i]))
        else:
            for numberText in numbersText:
                if string[i:(i+len(numberText))] == numberText:
                    return(numbersText.index(numberText) + 1)

def getSecondNumberPart2(string):
    for i in range(len(string) - 1, -1, -1):
        if string[i].isnumeric():
            return(int(string[i]))
        else:
            for numberText in numbersText:
                if string[i-len(numberText):i] == numberText:
                    return(numbersText.index(numberText) + 1) 

def runPart2(data):
    totalSum = int(0)
    for lineIndex in range(0, len(data)):
        line = data[lineIndex]
        totalSum += (getFirstNumberPart2(line) * 10) + getSecondNumberPart2(line)
    return(totalSum)

# Execute
print("Part 2")
print("Test:", runPart2(test))
print("Data:", runPart2(data))
