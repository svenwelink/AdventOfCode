import utils

test = utils.importData("TestInput/day01.txt")
input = utils.importData("Input/day01.txt")

def splitDirectionAndAmount(stringValue):
    return(stringValue[0], int(stringValue[1:]))

def runPartOne(data):
    dialValue, timesZeroPassed = 50, 0

    for instruction in data:
        direction, amount = splitDirectionAndAmount(instruction)

        # add the amount
        if direction == "R":
            dialValue += amount
        elif direction == "L":
            dialValue -= amount
        
        # check if 0 is passed
        if dialValue < 0 or dialValue > 99:
            dialValue = dialValue % 100

        # check if value is zero
        if dialValue == 0:
            timesZeroPassed += 1
    
    return(timesZeroPassed)
        
print(runPartOne(input))

def checkIfZeroIsPassed(timesZeroPassed, dialValue, amount):
    # check if 0 is passed
    if dialValue == 0:
         timesZeroPassed += 1

    elif dialValue < 0:
    # if the value was previusly zero
        if dialValue + amount == 0: 
            timesZeroPassed += (dialValue * -1 // 100) 
            dialValue = dialValue % 100
        # if extra turns are done
        else:
            timesZeroPassed += dialValue * -1 // 100 + 1
            dialValue = dialValue % 100
                
    elif dialValue > 99:
        timesZeroPassed += dialValue // 100
        dialValue = dialValue % 100

    return(timesZeroPassed, dialValue)

def runPartTwo(data):
    dialValue, timesZeroPassed = 50, 0

    for instruction in data:
        direction, amount = splitDirectionAndAmount(instruction)

        # add the amount
        if direction == "R":
            dialValue += amount
        elif direction == "L":
            dialValue -= amount

        timesZeroPassed, dialValue = checkIfZeroIsPassed(timesZeroPassed, dialValue, amount)

    return(timesZeroPassed)

print(runPartTwo(input))
