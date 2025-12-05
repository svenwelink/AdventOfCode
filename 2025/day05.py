import utils

test = utils.importData("TestInput/day05.txt")
input = utils.importData("Input/day05.txt")

def prepData(data):
    ranges, ingredients, rangesDone = [], [], False
    for row in data:
        row = row.strip()
        if not rangesDone:
            if row != "":
                ranges.append([int(x) for x in row.split("-")])
            else: rangesDone = True
        else: ingredients.append(int(row))

    return ranges, ingredients

def checkIfitemInList(item, ranges):
    for range in ranges:
        if item > range[0]:
            if item < range[1] + 1:
                return True
    return False

def runPartOne(data, freshCount = 0):
    ranges, ingredients = prepData(data)
    for x in ingredients:
        if checkIfitemInList(x, ranges):
            freshCount += 1
    return freshCount

print(runPartOne(input))

def checkIfItemsDontOverlap(item1, item2, tryReverse = True):
    if item1[0] < item2[0] and item1[1] < item2[0]:
        return True
    elif tryReverse:
        return checkIfItemsDontOverlap(item2, item1, tryReverse = False)
    return False

def getRangeWithoutOverlap(used, new): # 10,14 - 12,18
    nullValue = [0, -1]
    if new == nullValue:
        return nullValue
    elif used[0] <= new[0] and used[1] >= new[0]: # 10,14 - 12,18
        return [used[1]+1, new[1]]
    elif used[0] <= new[1] and used[1] >= new[1]: # 16,20 - 12, 18
        return [new[0], used[0] - 1]
    elif used == new:
        return nullValue
    #WERKT NOG NIET GOED EN LELIJKE CODE
    elif used[0] > new[0] and used[1] < new[1]:
        return [[new[0], used[0] - 1] , used[1] + 1, new[1]]
    return new
    
def runPartTwo(data, freshCount = 0):
    ranges, checkedRangeList = prepData(data)[0], []

    for rangeList in ranges:
        itemRanges = [rangeList] #[[3, 5], [7, 9]]

        for checked in checkedRangeList:
            for i in range(len(itemRanges)):
                if checkIfItemsDontOverlap(checked, itemRanges[i]) == False:
                    itemRanges[i] = getRangeWithoutOverlap(checked, itemRanges[i])

        for rangeX in itemRanges:
            freshCount += rangeX[1] - rangeX[0] + 1

        checkedRangeList.append(rangeList)
    return freshCount

print(runPartTwo(input))
