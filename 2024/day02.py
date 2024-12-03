import utils

df = utils.importData('')

# part 1
def getNumberList(string):
  x = string.split()
  x = [int(i) for i in x]
  return x

def checkForFalseDoubles(xList):
  if len(xList) == len(list(set(xList))):
    return True
  return False

def checkSorted(xList):
  sortedList = xList.copy()
  sortedList.sort()
  if xList == sortedList:
    return True

  else:
    sortedList.reverse()
    if xList == sortedList:
      return True

  return False

def getMaxDiff(xList):
  res = [abs(xList[i + 1] - xList[i]) for i in range(len(xList)-1)]
  return(max(res))

count = 0

for row in df:
  numbers = getNumberList(row)
  if checkForFalseDoubles(numbers):
    if checkSorted(numbers):
      if getMaxDiff(numbers) < 4:
        count += 1

print(count)

# part 2
def getDirectionId(xList, id):
  if xList[id] < xList[id+1]:
    return 'up'
  elif xList[id] > xList[id+1]:
    return 'down'
  
def getDirection(xList):
  up, down = 0, 0
  for i in range(3):
    if getDirectionId(xList, i) == 'up':
      up += 1
    elif getDirection(xList, i) == 'down':
      down += 1

  if up > 1: return 'up'
  else: return 'down'

count = 0

for row in df:
  numbers, notFound,  = getNumberList(row), True

  if checkForFalseDoubles(numbers):
    if checkSorted(numbers):
      if getMaxDiff(numbers) < 4:
        count += 1
        notFound = False
  
  indexId = 0
  while notFound and indexId < len(numbers):
    # try to pop numbers and check is list is good
    copyNumbers = numbers.copy()
    copyNumbers.pop(indexId)
    if checkForFalseDoubles(copyNumbers):
        if checkSorted(copyNumbers):
            if getMaxDiff(copyNumbers) < 4:
                count += 1
                notFound = False

    indexId += 1

print(count)
