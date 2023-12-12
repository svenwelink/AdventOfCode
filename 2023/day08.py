# Day 8
print("Day 8")

finalPosition = 'ZZZ'

def importData(path):
    file = open(path,'r')
    data = file.readlines()
    file.close()
    return(data)

pathFileData = # path
pathFileTestData = # Path
data = importData(pathFileData)
test = importData(pathFileTestData)

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
resultOne = runPartOne(data)
print("Result:", resultOne)

# Part 2
# Still needs some work
