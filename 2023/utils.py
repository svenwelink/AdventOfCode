# Changed since day 7 into loading both files
# Import data
def importData(path):
    file = open(path,'r')
    data = file.readlines()
    file.close()
    return(data)

pathFileData = #path
pathFileTestData = #path
data = importData(pathFileData)
test = importData(pathFileTestData)

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
