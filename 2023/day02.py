# Day 2
import utils

test = utils.importData("2023/TestInput/day02.txt")
data = utils.importData("2023/Input/day02.txt")

resetValue, nextValue = ";", ","

def runGame(line):
    gameId, game = line[5:].split(":")
    gameParts = game.split(resetValue)

    for i in range (0, len(gameParts)):
        grabs = gameParts[i].split(nextValue)

        for j in range(0, len(grabs)):
            grab = grabs[j].split(" ")
            

            if grab[2][0:3] == "red" and int(grab[1]) > 12:
                return(0)
            elif grab[2][0:5] == "green" and int(grab[1]) > 13:
                return(0)
            elif grab[2][0:4] == "blue" and int(grab[1]) > 14:
                return(0)

    return(int(gameId))

def runPartOne():
    totalSum = 0
    for lineId in range(0, len(data)):
        score = runGame(data[lineId])
        if score > 0:
            totalSum += score

    return(totalSum)

print("Day 2")
print("Part 1")
resultPartOne = runPartOne()
print(resultPartOne)

# Part 2
def runGamePartTwo(line):
    gameId, game = line[5:].split(":")
    gameParts = game.split(resetValue)
    minRed, minGreen, minBlue = 0, 0, 0

    for i in range (0, len(gameParts)):
        grabs = gameParts[i].split(nextValue)

        for j in range(0, len(grabs)):
            grab = grabs[j].split(" ")
        
            if grab[2][0:3] == "red":
                minRed = max(minRed, int(grab[1]))
            elif grab[2][0:5] == "green":
                minGreen = max(minGreen, int(grab[1]))
            elif grab[2][0:4] == "blue":
                minBlue = max(minBlue, int(grab[1]))

    product = minRed * minGreen * minBlue
    return(int(product))

def runPartTwo():
    totalSum = 0
    for lineId in range(0, len(data)):
        score = runGamePartTwo(data[lineId])
        totalSum += score

    return(totalSum)

print("Day 2")
print("Part 2")
resultPartTwo = runPartTwo()
print(resultPartTwo)
