import utils

input = utils.importData("Input/day03.txt")

def nextPos(currentPos, sign):
    if sign == "^":  
        currentPos[0] += 1
    elif sign == "v":
        currentPos[0] -= 1
    elif sign == "<":
        currentPos[1] -= 1
    else:
        currentPos[1] += 1
    return currentPos

def runPartOne(posVisited = [[0,0]], currentPos = [0, 0]):
    for sign in input[0]:
        currentPos = nextPos(currentPos, sign)
        if currentPos not in posVisited:
            posVisited.append(currentPos.copy())

    return(len(posVisited))

print(runPartOne())

def runPartTwo(posVisited = [[0,0]], currentPosSanta = [0, 0], currentPosRobot = [0,0]):
    for signId in range(len(input[0])):
        sign = input[0][signId]
        if signId % 2 == 0:
            currentPosSanta = nextPos(currentPosSanta, sign)
            if currentPosSanta not in posVisited:
                posVisited.append(currentPosSanta.copy())
        else:
            currentPosRobot = nextPos(currentPosRobot, sign)
            if currentPosRobot not in posVisited:
                posVisited.append(currentPosRobot.copy())

    return(len(posVisited))

print(runPartTwo())
