# Day 10
print("Day 10")

import utils

test = utils.importData("2023/TestInput/day.txt")
data = utils.importData("2023/Input/day.txt")

def getGridAndStartPos(data):
    df = []
    for i in range(len(data)):
        row = data[i].strip()
        dfRow = []
        for j in range(len(row)):
            dfRow.append(row[j])
            if row[j] == "S":
                startCoords = [i, j]

        df.append(dfRow)
    return(df, startCoords)

def getSecondPos(data, coords):
    coordsNew = coords
    # Check up
    if coords[0] >= 1 and (data[coords[0] - 1][coords[1]] == "|" or data[coords[0] - 1][coords[1]] == "F" or data[coords[0] - 1][coords[1]] == "7"):
        coordsNew[0] = coords[0] - 1
    # Check down
    elif coords[0] < len(data) and (data[coords[0] + 1][coords[1]] == "|" or data[coords[0] + 1][coords[1]] == "L" or data[coords[0] + 1][coords[1]] == "J"):
        coordsNew[0] = coords[0] + 1
    # Check left
    elif coords[1] >= 1 and(data[coords[0]][coords[1] - 1] == "-" or data[coords[0]][coords[1] - 1] == "F" or data[coords[0]][coords[1] - 1] == "L"):
        coordsNew[1] = coords[1] - 1
    else:
        coordsNew[1] = coords[1] + 1

    return(coordsNew)

def getNextPos(data, posMinusOne, pos):
    directionCharacter = data[pos[0]][pos[1]]

    if directionCharacter == "|":
        if pos[0] < posMinusOne[0]:
            newPos = [pos[0] - 1, pos[1]]
        else:
            newPos = [pos[0] + 1, pos[1]]
    elif directionCharacter == "-":
        if pos[1] < posMinusOne[1]:
            newPos = [pos[0], pos[1] - 1]
        else:
            newPos = [pos[0], pos[1] + 1]
    elif directionCharacter == "F":
        if pos[0] < posMinusOne[0]:
            newPos = [pos[0], pos[1] + 1]
        else:
            newPos = [pos[0] + 1, pos[1]]
    elif directionCharacter == "7":
        if pos[0] < posMinusOne[0]:
            newPos = [pos[0], pos[1] - 1]
        else: 
            newPos = [pos[0] + 1, pos[1]]
    elif directionCharacter == "J":
        if pos[0] > posMinusOne[0]:
            newPos = [pos[0], pos[1] - 1]
        else:
            newPos = [pos[0] - 1, pos[1]]
    else:
        if pos[0] > posMinusOne[0]:
            newPos = [pos[0], pos[1] + 1]
        else:
            newPos = [pos[0] - 1, pos[1]]  

    return(pos, newPos)

def runPartOne(data):
    frame, posMinusOne = getGridAndStartPos(data)
    pos = getSecondPos(frame, [posMinusOne[0], posMinusOne[1]])
    steps = 1

    while frame[pos[0]][pos[1]] != "S":
        posMinusOne, pos = getNextPos(frame, posMinusOne, pos)
        steps +=1

    return(int(steps/2))

print("Part 1")
#TestOne = runPartOne(test)
#print("Test one:", TestOne)
ResultOne = runPartOne(data)
print("Result part one:", ResultOne)

# Part 2

# Shoe lace formula:
# https://en.wikipedia.org/wiki/Shoelace_formula
# Pick's theorie
# https://en.wikipedia.org/wiki/Pick%27s_theorem

def getDeterminant(pointOne, pointTwo):
    det = pointOne[0] * pointTwo[1] - pointOne[1] * pointTwo[0]
    return(det)

def runPartTwo(data):
    frame, posMinusOne = getGridAndStartPos(data)
    pos = getSecondPos(frame, [posMinusOne[0], posMinusOne[1]])
    steps = 1
    determinantSum = getDeterminant(pos, posMinusOne)

    while frame[pos[0]][pos[1]] != "S":
        posMinusOne, pos = getNextPos(frame, posMinusOne, pos)
        determinantSum += getDeterminant(pos, posMinusOne)
        steps +=1

    area = abs(determinantSum / 2)

    # Picks theorem:
    innerPoints = int((area - (steps / 2)) + 1)
    return(innerPoints)

print("Part 2")
resultTwo = runPartTwo(data)
print("Result:", resultTwo)
