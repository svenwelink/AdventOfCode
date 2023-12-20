# Day 6
print("Day 6")

import utils

test = utils.importData("2023/TestInput/day06.txt")
data = utils.importData("2023/Input/day06.txt")

def removeSpacesList(list):
    list = ' '.join(list).split()
    return(list)

def changeStringListToInterger(numberList):
    numberList = list(map(int, numberList))
    return(numberList)

def getListFromRow(row):
    header, data = row.split(":")
    dataList = data.split(" ")
    dataList = removeSpacesList(dataList)
    dataList = changeStringListToInterger(dataList)
    return(dataList) 

def getProductFromList(listProduct):
    product = 1
    for i in listProduct:
        product = product * i
    return(product) 

def runPartOne():
    timeList, distanceList = getListFromRow(data[0]), getListFromRow(data[1])
    newRecordList = []

    for i in range(len(timeList)):
        maxTime = int(timeList[i])
        recordCount = 0

        for xSeconds in range(maxTime):
            speed, timeToRace = int(xSeconds), (maxTime - int(xSeconds))
            distance = speed * timeToRace
            if distance > distanceList[i]:
                recordCount += 1

        newRecordList.append(int(recordCount))

    # After all racing is done calculate score from newRecordList
    return(getProductFromList(newRecordList))

print("part 1")
resultPartOne = runPartOne()
print(resultPartOne)

# Part 2
def getValueFromRow(row):
    header, data = row.split(":")
    data = int(data.replace(" ", ""))
    return(data) 

def getFirstTimeBeatDistance(time, distance):
    for speed in range(time):
        remainingTime = time - speed
        totalDistance = speed * remainingTime
        if totalDistance > distance:
            return(speed)
        
    print("No speed found to beat record")
    return(False)

def runPartTwo():
    timeSlots, distanceToBeat = getValueFromRow(data[0]), getValueFromRow(data[1])

    firstTimeBeat = getFirstTimeBeatDistance(timeSlots, distanceToBeat)
    lastTimeToBeat = timeSlots - firstTimeBeat
    
    totalBeatTimes = lastTimeToBeat - firstTimeBeat + 1
    return(totalBeatTimes)

print("part 2")
resultTwo = runPartTwo()
print(resultTwo)
