import utils

input = utils.importData("Input/day01.txt")[0]

def getTheRightFloor(sign):
    if sign == ")": 
        return -1
    return 1

def runPartOne(data, height=0):
    for i in range(len(data)):
        height += getTheRightFloor(data[i])
    return height

print(runPartOne(input))
        
def runPartTwo(data, height=0):
    for i in range(len(data)):
        height += getTheRightFloor(data[i])
        if height == -1: 
            return i + 1
    return len(data)

print(runPartTwo(input))
