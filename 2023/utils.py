def importData(path):
    file = open(path,'r')
    data = file.readlines()
    file.close()
    return(data)

def getRawFrame(data):
    frame = []
    for i in range(len(data)):
        rowFrame = []
        row = r"{}".format(data[i]).strip()
        
        for j in range(len(row)):
            if len(row[j]) > 0:
                rowFrame.append(row[j])
                
        frame.append(rowFrame)
    return(frame)

def removeSpacesList(list):
    list = ' '.join(list).split()
    return(list)

def changeStringListToInterger(numberList):
    numberList = list(map(int, numberList))
    return(numberList)

def getProductFromList(listProduct):
    product = 1
    for i in listProduct:
        product = product * i
    return(product) 

def transposeList(frame):
  transposedFrame = []
  for columnId in range(len(frame[0])):
    newRow = ""
    for rowId in range(len(frame)):
      newRow += frame[rowId][columnId]
    transposedFrame.append(newRow)
  return(transposedFrame)
