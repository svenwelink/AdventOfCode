print("Day 5")
# Import data
import utils

test = utils.importData("2023/TestInput/day05.txt")
data = utils.importData("2023/Input/day05.txt")

def removeSpacesList(list):
    list = ' '.join(list).split()
    return(list)

def changeStringListToInterger(numberList):
    numberList = list(map(int, numberList))
    return(numberList)

def getSeedsList():
    seed, string = data[0]. split(":")
    stringList = string.split(" ")
    stringList = removeSpacesList(stringList)
    intergerList = changeStringListToInterger(stringList)
    return(intergerList)

def getAllMaps():
    dataList, newMap = [], []

    for i in range(1, len(data)):
        if len(data[i]) == 1: 
            if len(newMap) > 0:
                dataList.append(newMap)
            newMap = []
        elif data[i][0].isnumeric():
            rowList = data[i].split(" ")
            rowListWithoutSpaces = removeSpacesList(rowList)
            rowListIntergers = changeStringListToInterger(rowListWithoutSpaces)
            newMap.append(rowListIntergers)
    dataList.append(newMap)
    return(dataList)

def runPartOne():
    seeds = getSeedsList()
    allMaps = getAllMaps()

    for map in allMaps:
        seedNotToNextMap = [True] * len(seeds)
        for mapRow in map:
            rangeLow, rangeHigh = mapRow[1], mapRow[1] + mapRow[2]
            
            for seedId in range(len(seeds)):
                if seeds[seedId] >= rangeLow and seeds[seedId] < rangeHigh and seedNotToNextMap[seedId]:
                    seeds[seedId] += mapRow[0] - mapRow[1]
                    seedNotToNextMap[seedId] = False     
    minSeeds = min(seeds)
    return(minSeeds)

print("Part 1")
print(runPartOne())

# Part 2

def runPartTwoReversed():
    seedFound = True
    seedListRanges = getSeedsList()
    allMaps = getAllMaps()
    allMaps.reverse()

    location, calcSeed = 1, 1
    while seedFound:
        if location % 100000 == 0:
            print(location/1000000, "mil")

        for map in allMaps:
            mapNotUsed = True
            for mapRow in map:
                if calcSeed >= mapRow[0] and calcSeed < mapRow[0] + mapRow[2] and mapNotUsed:
                    mapNotUsed = False
                    calcSeed += (mapRow[1] - mapRow[0])
        
        for seedRangeId in range(0, len(seedListRanges), 2):
            if calcSeed >= seedListRanges[seedRangeId] and calcSeed < (seedListRanges[seedRangeId] + seedListRanges[seedRangeId + 1]):
                return(location)

        location += 1
        calcSeed = location

print("Part 2")
print(runPartTwoReversed())
