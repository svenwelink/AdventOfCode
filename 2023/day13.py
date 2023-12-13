# Day 13
print("Day 13")
# Import data
def importData(path):
    file = open(path,'r')
    data = file.readlines()
    file.close()
    return(data)

pathFileData = # Path
pathFileTestData = # Path
data = importData(pathFileData)
test = importData(pathFileTestData)

def runPartOne(data):
  mirrorPoints = 0
  lastWhiteLineIndex = 0
  for i in range(len(data)):
    if len(data[i].strip()) == 0:
      frame = getFrame(data, lastWhiteLineIndex, i)
      mirrorPoints += getPointsFrame(frame)
      lastWhiteLineIndex = i
  return(mirrorPoints)

def getFrame(data, firstRow, lastRowPlusOne):
  frame = []
  for i in range(firstRow, lastRowPlusOne):
    row, rowList = data[i].strip(), []
    for j in range(len(row)):
      rowList.append(row[j])
    frame.append(row)
  return(frame)

def getPointsFrame(frame):
  for rowId in range(1, len(frame) - 1):
    rowsToCheck = min(rowId + 1, len(frame))

# Needs to be finished
