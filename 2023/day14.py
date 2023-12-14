# Day 14
print("Day 14")

# Import data
def importData(path):
    file = open(path,'r')
    data = file.readlines()
    file.close()
    return(data)

pathFileData = "C:/Users/svenw/Documents/ProgrammeerProjecten/Advent/2023/day14/input.txt"
pathFileTestData = "C:/Users/svenw/Documents/ProgrammeerProjecten/Advent/2023/day14/inputTest.txt"
data = importData(pathFileData)
test = importData(pathFileTestData)

pillar = "#"
rock = "O"

def tiltToNorth(frame):
  transposedFrame = []
  for columnId in range(len(frame[0])):
    newRow = []
    for rowId in range(len(frame)):
      newRow += frame[rowId][columnId]
    transposedFrame.append(newRow)
  return(transposedFrame)

def makeFrame(data):
    frameList = []
    for i in range(len(data)):
        row = []
        inputRow = data[i].strip()

        for j in range(len(inputRow)):
            row.append(inputRow[j])

        frameList.append(row)
    return(frameList)

def calculateColumnPoints(columnList):
    columnSum, lastRockIndex, rockCount = 0, -1, 0
    
    for i in range(len(columnList)):
        if columnList[i] == pillar:
            while rockCount > 0:
                columnSum += len(columnList) - lastRockIndex - 1
                rockCount -= 1
                lastRockIndex += 1
            lastRockIndex = i
        elif columnList[i] == rock:
           rockCount += 1
    
    while rockCount > 0:
                columnSum += len(columnList) - lastRockIndex - 1
                rockCount -= 1
                lastRockIndex += 1

    return(columnSum)
      
def runPartOne(data):
    totalSum = 0
    frame = makeFrame(data)
    tiltedFrame = tiltToNorth(frame)

    for i in range(len(tiltedFrame)):
      totalSum += calculateColumnPoints(tiltedFrame[i])

    return(totalSum)

print("Part 1")
print("Test:", runPartOne(test))
print("Test:", runPartOne(data))

# Part two need to be done
