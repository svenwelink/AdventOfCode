import utils
import itertools

test = utils.importData("TestInput/day10.txt")
input = utils.importData("Input/day10.txt")

def getSolution(solutinString):
    solutionList = []
    for i in range(1, len(solutinString)):
        if solutinString[i] == ".":
            solutionList.append(0)
        elif solutinString[i] == "#":
            solutionList.append(1)
    return solutionList

def getButtonEffect(buttonEffectsString, lampCount):
    buttonEffect = []
    effectlist = [int(x) for x in buttonEffectsString[1:-1].split(",")]

    for lamp in range(lampCount):
        if lamp in effectlist:
            buttonEffect.append(1)
        else: buttonEffect.append(0)
    return buttonEffect

def translateInputStringToLPInput(string):
    splitedList = string.strip().split(" ")
    buttonsList = []
    for element in splitedList:
        if element[0] == "[":
            solution = getSolution(element)
            lampCount = len(solution)
        elif element[0] == "(":
            buttonsList.append(getButtonEffect(element, lampCount))
        elif element[0] == "{":
            joltageScheme = [int(x) for x in element[1:-1].split(",")]
    return solution, buttonsList, joltageScheme

def calculatCombination(combination):
    if len(combination) == 1:
        return combination
    newCombination = combination[0]
    for button in combination[1:]:
        for id in range(len(combination)):
            newCombination[id] += button[id]
    return newCombination

def combinationIsGood(solution, combination):
    for id in range(len(solution)):
        if combination[id] % 2 != solution[id]:
            return False
    return True

def getAllCombinations(buttons):
    buttonCombinations = []
    for i in range(1, len(buttons) + 1):
        buttonCombinations.append(list(itertools.combinations([x for x in range(len(buttons))], i)))
    print(buttonCombinations)
    return list(itertools.combinations(buttons, len(buttons)))

def getMinimumButtonPressesForSolution(solution, buttons):
    combinations = getAllCombinations(buttons)
    print(combinations)
    for combination in combinations:
        print(combination)
        combinationSolution = calculatCombination(combination)
        if combinationIsGood(solution, combinationSolution):
            return len(combination)
    return len(solution)

def runPartOne(data):
    totalPresses = 0
    for i in data:
        solution, buttons = translateInputStringToLPInput(i)[:2]
        totalPresses += getMinimumButtonPressesForSolution(solution, buttons)

    return totalPresses

runPartOne(test)
