import utils

test = utils.importData("TestInput/day04.txt")
input = utils.importData("Input/day04.txt")

def isRollAccessible(df, pos):
    if df[pos[0]][pos[1]] == ".":
        return False
    
    stringAroundPos = str(df[pos[0]-1][(pos[1]-1):(pos[1]+2)]) + str(df[pos[0]][pos[1]-1]) + str(df[pos[0]][pos[1]+1]) + str(df[pos[0]+1][(pos[1]-1):(pos[1]+2)])
    if stringAroundPos.count("@") < 4:
        return True

    return False

def runPartOne(data, totalCount = 0):
    diagram = utils.addPaddingToFrame(data, sign=".")
    for x in range(1, len(diagram)-1): 
        for y in range(1, len(diagram[x])):
            if isRollAccessible(diagram, [x, y]):
                totalCount += 1

    return totalCount

print(runPartOne(input))

def runPartTwo(data, totalCount = 0, removedLastRound = 1):
    diagram = utils.addPaddingToFrame(data, sign=".")
    while removedLastRound > 0:
        removedLastRound = 0
        for x in range(1, len(diagram)-1): 
            for y in range(1, len(diagram[x])):
                if isRollAccessible(diagram, [x, y]):
                    diagram[x][y] = "."
                    removedLastRound += 1

        totalCount += removedLastRound

    return totalCount

print(runPartTwo(input))
