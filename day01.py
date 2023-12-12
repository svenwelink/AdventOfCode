# Day 01
# Part 1
# Functions
def importData(path):
    file = open(pathFile,'r')
    data = file.readlines()
    file.close()
    return(data)

def getFirstNumber(string):
    for i in range(0, len(string)):
        if string[i].isnumeric():
            return(int(string[i]))

def getSecondNumber(string):
    for i in range(len(string) - 1, -1, -1):
        if string[i].isnumeric():
            return(int(string[i]))
        
def runPart1():
    totalSum = int(0)
    for lineIndex in range(0, len(data)):
        line = data[lineIndex]
        totalSum += (getFirstNumber(line) * 10) + getSecondNumber(line)
    return(totalSum)

# Execute
print("Day 1")

# Import data
pathFile = # Path to data
data = importData(pathFile)

resultPart1 = runPart1()
print("Part 1")
print(resultPart1)

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

def runPart2():
    totalSum = int(0)
    for lineIndex in range(0, len(data)):
        line = data[lineIndex]
        totalSum += (getFirstNumberPart2(line) * 10) + getSecondNumberPart2(line)
    return(totalSum)

# Execute
resultPart2 = runPart2()
print("Part 2")
print(resultPart2)
