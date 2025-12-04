import utils

test = utils.importData("TestInput/day04.txt")
input = utils.importData("Input/day04.txt")

def turnStringIntoList(row):
    return [row[x] for x in range(len(row))]

def prepDiagram(data):
    df = [x.strip().replace(".", "0").replace("@", "1") for x in data]
    padddingRow = turnStringIntoList("0" * (len(df[0]) + 2))
    frameWithPadding = []
    frameWithPadding.append(padddingRow)
    for i in range(len(df)):
        frameWithPadding.append(turnStringIntoList("0" + df[i] + "0"))
    frameWithPadding.append(padddingRow)
    
    return frameWithPadding

def isRollAccessible(df, pos):
    if df[pos[0]][pos[1]] == "0":
        return False
    
    stringAroundPos = str(df[pos[0]-1][(pos[1]-1):(pos[1]+2)]) + str(df[pos[0]][pos[1]-1]) + str(df[pos[0]][pos[1]+1]) + str(df[pos[0]+1][(pos[1]-1):(pos[1]+2)])
    if stringAroundPos.count("1") < 4:
        return True

    return False

def runPartOne(data, totalCount = 0):
    diagram = prepDiagram(data)
    for x in range(1, len(diagram)-1): 
        for y in range(1, len(diagram[x])):
            if isRollAccessible(diagram, [x, y]):
                totalCount += 1

    return totalCount

print(runPartOne(input))

def runPartTwo(data, totalCount = 0, removedLastRound = 1):
    diagram = prepDiagram(data)
    while removedLastRound > 0:
        removedLastRound = 0
        for x in range(1, len(diagram)-1): 
            for y in range(1, len(diagram[x])):
                if isRollAccessible(diagram, [x, y]):
                    diagram[x][y] = "0"
                    removedLastRound += 1

        totalCount += removedLastRound

    return totalCount

print(runPartTwo(input))
