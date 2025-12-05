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

class rangeInstruction:
    def __init__(self, values):
        self.lowestValue = values[0]
        self.highestValue = values[1]
        self.needToDalculateLength = True
        self.needsToBeSplit = False

    def getLength(self):
        if self.needToDalculateLength:
            return self.highestValue - self.lowestValue + 1
        else: return 0
    
    def changeHighest(self, newHighest):
        self.highestValue = newHighest
        
    def changeLowest(self, newLowest):
        self.lowestValue = newLowest
    
    def splitInTwo(self):
        self.needsToBeSplit = True

    def noCalculationNeeded(self):
        self.needToDalculateLength = False

def ItemsDontOverlap(item1:rangeInstruction, item2:rangeInstruction, tryReverse = True):
    if item1.lowestValue < item2.lowestValue and item1.highestValue < item2.lowestValue:
        return True
    elif tryReverse:
        return ItemsDontOverlap(item2, item1, tryReverse = False)
    return False

def leftSideOverlap(used:rangeInstruction, toCheck:rangeInstruction):
    if used.lowestValue <= toCheck.lowestValue:
        if used.highestValue >= toCheck.lowestValue:
            if used.highestValue < toCheck.highestValue:
                return True
    return False

def rightSideOverlap(used:rangeInstruction, toCheck:rangeInstruction): #5,10 2, 8
    if used.lowestValue <= toCheck.highestValue:
        if used.highestValue >= toCheck.highestValue:
            if used.lowestValue > toCheck.lowestValue:
                return True
    return False

def instructionsAreFullyOverlapped(used:rangeInstruction, toCheck:rangeInstruction):
    if used.lowestValue <= toCheck.lowestValue:
        if used.highestValue >= toCheck.highestValue:
            return True
    return False

def needToSplitNewRange(used:rangeInstruction, toCheck:rangeInstruction):
    if used.lowestValue > toCheck.lowestValue:
        if used.highestValue < toCheck.highestValue:
            return True
    return False

def getRangeWithoutOverlap(used:rangeInstruction, toCheck:rangeInstruction):
    if toCheck.needToDalculateLength == False:
        return toCheck
    elif ItemsDontOverlap(used, toCheck):
        return toCheck
    elif leftSideOverlap(used, toCheck):
        toCheck.changeLowest(used.highestValue + 1)
    elif rightSideOverlap(used, toCheck):
        toCheck.changeHighest(used.lowestValue - 1)
    elif instructionsAreFullyOverlapped(used, toCheck):
        toCheck.noCalculationNeeded()
    elif needToSplitNewRange(used, toCheck):
        toCheck.splitInTwo()
    return toCheck

def splitNewRangeWithOldRange(used:rangeInstruction, toCheck:rangeInstruction):
    range1 = rangeInstruction([toCheck.lowestValue, used.lowestValue - 1])
    range2 = rangeInstruction([used.highestValue + 1, toCheck.highestValue])
    return range1, range2
    
def runPartTwo(data, freshCount = 0):
    ranges, checkedRangeList = prepData(data)[0], []
    rangeObjects = [rangeInstruction(x) for x in ranges]
    for instruction in rangeObjects:
        if len(checkedRangeList) > 0:
            for checked in checkedRangeList:
                instruction = getRangeWithoutOverlap(checked, instruction)

                if instruction.needsToBeSplit:
                    instruction, instructionAddToList = splitNewRangeWithOldRange(checked, instruction)
                    rangeObjects.append(instructionAddToList)
        
        checkedRangeList.append(instruction)
        if instruction.needToDalculateLength:
            freshCount += int(instruction.getLength())
            
    return freshCount

print(runPartTwo(input))
