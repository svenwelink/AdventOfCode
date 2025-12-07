import utils

test = [x.strip() for x in utils.importData("TestInput/day07.txt")]
input = [x.strip() for x in utils.importData("Input/day07.txt")]

def getIndexOfValues(stringInput, value):
    return [x for x in range(len(stringInput)) if stringInput[x] == value]

def getUniqueValuesOfList(multList):
    uniqueSet = set(multList)
    return list(uniqueSet)

def runPartOne(data, splitCount = 0):
    pointsToSplit = [utils.turnStringIntoList(data[0]).index("S")]

    for i in range(2, len(data), 2):
        rowSplitters, newStreams = getIndexOfValues(data[i], "^"), []
        for stream in pointsToSplit:
            if stream in rowSplitters:
                newStreams.append(stream - 1)
                newStreams.append(stream + 1)
                splitCount += 1
            else:
                newStreams.append(stream)

        pointsToSplit = getUniqueValuesOfList(newStreams)
    return splitCount

print(runPartOne(input))

class splitPoint:
    def __init__(self, values):
        self.index = values[0]
        self.paths = values[1]

def runPartTwo(data):
    pointsToSplit = [splitPoint([utils.turnStringIntoList(data[0]).index("S"), 1])]

    for i in range(2, len(data), 2):
        rowSplitters, newStreams = getIndexOfValues(data[i], "^"), []
        for stream in pointsToSplit:
            if stream.index in rowSplitters:
                newStreams.append(splitPoint([stream.index - 1, stream.paths]))
                newStreams.append(splitPoint([stream.index + 1, stream.paths]))
            else:
                newStreams.append(stream)

        pointsToSplit = []        
        for stream in newStreams:
            if stream.index in [x.index for x in pointsToSplit]:
                for x in pointsToSplit:
                    if x.index == stream.index:
                        x.paths += stream.paths
            else:
                pointsToSplit.append(stream)

    return(sum([x.paths for x in pointsToSplit]))

print(runPartTwo(input))
