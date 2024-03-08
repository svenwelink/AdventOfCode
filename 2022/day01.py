print("2022 day 1")

import utils

test = utils.importData("test/day01.txt")
data = utils.importData("input/day01.txt")

class newBackpack:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def calculateTotalCalories(self):
        return(sum(self.items))

def runPartOne(df):
    allElves, elveBackpack = [], newBackpack()

    for i in range(len(df)):
        possibleItem = df[i].strip()
        if possibleItem.isnumeric():
            elveBackpack.addItem(int(possibleItem))
        else:
            allElves.append(elveBackpack.calculateTotalCalories())
            elveBackpack = newBackpack()
    allElves.append(elveBackpack.calculateTotalCalories())   
    return(max(allElves))

print("Part 1")
print(runPartOne(test))
print(runPartOne(data))

def runPartTwo(df):
    allElves, elveBackpack = [], newBackpack()

    for i in range(len(df)):
        possibleItem = df[i].strip()
        if possibleItem.isnumeric():
            elveBackpack.addItem(int(possibleItem))
        else:
            allElves.append(elveBackpack.calculateTotalCalories())
            elveBackpack = newBackpack()
    allElves.append(elveBackpack.calculateTotalCalories())   

    topThree = []
    for i in range(3):
        maxCalories = max(allElves)
        topThree.append(maxCalories)
        allElves.pop(allElves.index(maxCalories))

    return(sum(topThree))

print("Part 2")
print(runPartTwo(test))
print(runPartTwo(data))