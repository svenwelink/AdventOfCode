def importData(path):
    file = open(path,'r')
    data = file.readlines()
    file.close()
    return data

def getRawFrame(data):
    frame = []
    for i in range(len(data)):
        rowFrame = []
        row = r"{}".format(data[i]).strip()
        
        for j in range(len(row)):
            if len(row[j]) > 0:
                rowFrame.append(row[j])
                
        frame.append(rowFrame)
    return frame

def changeStringListToInterger(numberList):
    numberList = list(map(int, numberList))
    return numberList

def getProductFromList(listProduct):
    product = 1
    for i in listProduct:
        product = product * i
    return product

def transposeList(frame):
  transposedFrame = []
  for columnId in range(len(frame[0])):
    newRow = ""
    for rowId in range(len(frame)):
      newRow += frame[rowId][columnId]
    transposedFrame.append(newRow)
  return transposedFrame 

def turnStringIntoList(row):
    return [row[x] for x in range(len(row))]

def addPaddingToFrame(data, sign= "0"):
    df = [x.strip() for x in data]
    padddingRow = turnStringIntoList(sign * (len(df[0]) + 2))
    frameWithPadding = []
    frameWithPadding.append(padddingRow)
    for i in range(len(df)):
        frameWithPadding.append(turnStringIntoList(sign + df[i] + sign))
    frameWithPadding.append(padddingRow)
    
    return frameWithPadding

def stringAroundPositionIn2DList(df, pos):
    topRow = str(df[pos[0]-1][(pos[1]-1):(pos[1]+2)])
    middleRow = str(df[pos[0]][pos[1]-1]) + str(df[pos[0]][pos[1]+1])
    bottemRow = str(df[pos[0]+1][(pos[1]-1):(pos[1]+2)])
    fullString = topRow + middleRow + bottemRow
    return fullString
