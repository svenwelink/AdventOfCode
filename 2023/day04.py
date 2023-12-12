print("Day 4")
# Import data
def importData(path):
    file = open(pathFile,'r')
    data = file.readlines()
    file.close()
    return(data)

pathFile = # Input path
data = importData(pathFile)

print("Part 1")

def calculatePoints(winningNumbers):
    return(2**(winningNumbers - 1))

def getCardLists(cardRow):
    cardNumber, card = cardRow.split(":")
    cardWinningNumbers, cardNumbers = card.split("|")
    cardWinningNumberList = getNumberListFromString(cardWinningNumbers)
    cardNumbersList = getNumberListFromString(cardNumbers)
    return(cardWinningNumberList, cardNumbersList)

def getNumberListFromString(string):
    numbersListWithSpaces = string.split(" ")
    numbersListWithoutSpaces = removeSpacesList(numbersListWithSpaces)
    numbersListIntergers = changeStringListToInterger(numbersListWithoutSpaces)
    return(numbersListIntergers)

def removeSpacesList(list):
    list = ' '.join(list).split()
    return(list)

def changeStringListToInterger(numberList):
    numberList = list(map(int, numberList))
    return(numberList)

def runPartOne():
    totalScore = 0 
    for i in range(len(data)):
        totalWinningNumbers = 0
        winningNumbers, cardNumbers = getCardLists(data[i])

        for number in winningNumbers:
            if number in cardNumbers:
                totalWinningNumbers += 1
        
        if totalWinningNumbers > 0:
            totalScore += calculatePoints(totalWinningNumbers)
    return(totalScore)

print(runPartOne())

# Part 2
print("Part 2")

def makeCardList(length):
    cardList = []
    for i in range(length):
        cardList.append(1)
    return(cardList)

def getWinningNumberForCards():
    winningNumbersList = []
    for i in range(len(data)):
        totalWinningNumbers = 0
        winningNumbers, cardNumbers = getCardLists(data[i])

        for number in winningNumbers:
            if number in cardNumbers:
                totalWinningNumbers += 1
        winningNumbersList.append(totalWinningNumbers)
    return(winningNumbersList)

def runPartTwo():
    winningNumbersList = getWinningNumberForCards()
    cardListToEmpty = makeCardList(len(data))
    totalCards = []

    for i in range(len(cardListToEmpty)):
        totalCards.append(cardListToEmpty[i])

        for times in range(cardListToEmpty[i]):            
            for cardsToPlus in range(1, winningNumbersList[i] + 1):
                cardListToEmpty[i + cardsToPlus] += 1
    
    return(sum(totalCards))

print(runPartTwo())
