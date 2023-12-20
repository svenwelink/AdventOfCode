# Day 7

import pandas as pd
import utils

test = utils.importData("2023/TestInput/day07.txt")
data = utils.importData("2023/Input/day07.txt")

print("Day 7")

# cardValue of numbers is always lower then charachters
cardValueChar = ["T", "J", "Q", "K", "A"]
cardCombinations = ["Five of a kind",
                    "Four of a kind",
                    "Full house",
                    "Three of a kind",
                    "Two pair",
                    "One pair",
                    "High card"]

def getGameDataFrame(data):
    hands, bids, handType, handTypePower, cardsPowers = [], [], [], [], []

    for i in range(len(data)):
        hand, bid = data[i].split(" ")
        hands.append(hand)
        bids.append(int(bid.strip()))

        cardCombination = getCardCombination(hand)
        handType.append(cardCombination[0])
        handTypePower.append(cardCombination[1])

        cardPower = getCardsPower(hand)
        cardsPowers.append(cardPower)

    df = pd.DataFrame({"Hands": hands,
                       "Bids": bids,
                       "HandType": handType,
                       "HandTypePower": handTypePower,
                       "CardPower": cardsPowers})
    return(df)

def getCardCombination(hand):
    uniqueValuesHand = list(set(hand))
    # If only one type of card it is: Five of a kind
    if len(uniqueValuesHand) == 1:
        return(cardCombinations[0], 7)
    # If one value is counted four times it is: Four of a kind
    elif hand.count(uniqueValuesHand[0]) == 4 or hand.count(uniqueValuesHand[1]) == 4:
        return(cardCombinations[1], 6)
    # The only possiability with two different type of cards is: Full house
    elif len(uniqueValuesHand) == 2:
        return(cardCombinations[2], 5)
    # If five different cards then it is: High card
    elif len(uniqueValuesHand) == 5:
        return(cardCombinations[6], 1)
    # If four different cards it is : One pair
    elif len(uniqueValuesHand) == 4:
        return(cardCombinations[5], 2)
    # if one value is counted three times it is: Three of a kind
    elif hand.count(uniqueValuesHand[0]) == 3 or hand.count(uniqueValuesHand[1]) == 3 or hand.count(uniqueValuesHand[2]) == 3:
        return(cardCombinations[3], 4)
    # Else it is a two pair
    return(cardCombinations[4], 3)

def getCardsPower(hand):
    cardsPower = 0
    for i in range(len(hand)):
        card = hand[i]
        if card.isnumeric():
            cardsPower += int(card) * 100 ** (len(hand) - 1 - i)
        else:
            cardNumber = int(cardValueChar.index(card) + 10)
            cardsPower += cardNumber * 100 ** (len(hand) - 1 - i)
    return(cardsPower)

def runPartOne(data):
    df = getGameDataFrame(data)
    df = df.sort_values(["HandTypePower", "CardPower"], ascending = [True, True])
    df = df.reset_index(drop=True)
    df["Rank"] = df.index + 1
    df["Winning"] = df.apply(calculateWinnigs, axis = 1)

    totalWinnigs = df["Winning"].sum()
    return(totalWinnigs)

def calculateWinnigs(row):
    winnings = row.Rank * row.Bids
    return(winnings)

print("Part 1")
testResultOne = runPartOne(test)
print("Test result:", testResultOne)
resultOne = runPartOne(data)
print("Result:", resultOne)

# Part 2
cardValueCharPartTwo = ["J", "T", "Q", "K", "A"]

def getCardsPowerPartTwo(hand):
    cardsPower = 0
    for i in range(len(hand)):
        card = hand[i]
        if card.isnumeric():
            cardsPower += int(card) * 100 ** (len(hand) - 1 - i)
        else:
            cardNumber = int(cardValueCharPartTwo.index(card) * 10)
            cardsPower += cardNumber * 100 ** (len(hand) - 1 - i)
    return(cardsPower)

def getCardCombinationPartTwo(hand):
    newHand = hand.replace("J", "")
    jokerCount = len(hand) - len(newHand)
    uniqueValuesHand = list(set(newHand))
    # If only one type of card it is: Five of a kind
    if len(list(set(hand))) == 1:
        return(cardCombinations[0], 7)
    elif len(uniqueValuesHand) == 1:
        return(cardCombinations[0], 7)
    # If one value is counted four times it is: Four of a kind
    elif hand.count(uniqueValuesHand[0]) == (len(newHand) - 1) or hand.count(uniqueValuesHand[1]) == (len(newHand) - 1):
        return(cardCombinations[1], 6)
    # The only possiability with two different type of cards is: Full house
    elif len(uniqueValuesHand) == 2:
        return(cardCombinations[2], 5)
    # If five different cards then it is: High card
    elif len(uniqueValuesHand) == 5:
        return(cardCombinations[6], 1)
    # If four different cards it is : One pair
    elif len(uniqueValuesHand) == 4:
        return(cardCombinations[5], 2)
    # if one value is counted three times it is: Three of a kind
    elif checkThreeOfAKindWithJokers(newHand, jokerCount):
        return(cardCombinations[3], 4)
    # Else it is a two pair
    return(cardCombinations[4], 3)

def checkThreeOfAKindWithJokers(newHand, jokerCount):
    uniqueValuesHand = list(set(newHand))
    if jokerCount >= 2:
        return(True)
    elif jokerCount == 0:
        if newHand.count(uniqueValuesHand[0]) == 3 or newHand.count(uniqueValuesHand[1]) == 3 or newHand.count(uniqueValuesHand[2]) == 3:
            return(True)
    # Joker count is one
    elif newHand.count(uniqueValuesHand[0]) == 2 or newHand.count(uniqueValuesHand[1]) == 2 or newHand.count(uniqueValuesHand[2]) == 2:
        return(True)

    return(False)

def getGameDataFramePartTwo(data):
    hands, bids, handType, handTypePower, cardsPowers = [], [], [], [], []

    for i in range(len(data)):
        hand, bid = data[i].split(" ")
        hands.append(hand)
        bids.append(int(bid.strip()))

        cardCombination = getCardCombinationPartTwo(hand)
        handType.append(cardCombination[0])
        handTypePower.append(cardCombination[1])

        cardPower = getCardsPowerPartTwo(hand)
        cardsPowers.append(cardPower)

    df = pd.DataFrame({"Hands": hands,
                       "Bids": bids,
                       "HandType": handType,
                       "HandTypePower": handTypePower,
                       "CardPower": cardsPowers})
    return(df)

def runPartTwo(data):
    df = getGameDataFramePartTwo(data)
    df = df.sort_values(["HandTypePower", "CardPower"], ascending = [True, True])
    df = df.reset_index(drop=True)
    df["Rank"] = df.index + 1
    df["Winning"] = df.apply(calculateWinnigs, axis = 1)

    totalWinnigs = df["Winning"].sum()
    return(totalWinnigs)

print("Part 2")
testResultTwo = runPartTwo(test)
print("Test result:", testResultTwo)
resultTwo = runPartTwo(data)
print("Result:", resultTwo)
