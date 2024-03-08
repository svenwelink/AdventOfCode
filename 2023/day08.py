import utils

test = utils.importData("TestInput/day08.txt")
data = utils.importData("Input/day08.txt")
# Day 8
print("Day 8")

finalPosition = 'ZZZ'

def makeMappingLists(data):
    mapNameList, mapDirectionList = [], []
    for i in range(2, len(data)):
        inputRow = data[i]

        mapName = inputRow[0:3]
        mapDirection = [inputRow[7:10], inputRow[12:15]]

        mapNameList.append(mapName)
        mapDirectionList.append(mapDirection)

    return(mapNameList, mapDirectionList)

def runPartOne(data, position = 'AAA'):
    instructions = data[0]
    instructions =  instructions.strip().replace(" ", "")
    mapNameList, mapDirectionList = makeMappingLists(data)
    stepsDone = 0

    while position != finalPosition:
        positionInLists = mapNameList.index(position)

        if instructions[stepsDone % len(instructions)] == 'L':
            position = mapDirectionList[positionInLists][0]
        else:
            position = mapDirectionList[positionInLists][1]

        stepsDone += 1
    return(stepsDone)

print("Part one")
print("Result:", runPartOne(data))

# Part 2
# Still needs some work
