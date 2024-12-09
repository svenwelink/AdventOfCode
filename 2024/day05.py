import utils

df_input = utils.importData()
df = [x.strip() for x in df_input]

rules, pages = [],[]
addingRules = True
for line in df:
    if line == '':
        addingRules = False
    elif addingRules:
        rules.append(line)
    else:
        pages.append(line)

pages = [x.split(',') for x in pages]

def checkOfAllowed(page):
  for firstPage in range(len(page)):
    for secondPage in range(firstPage+1, len(page)):
      ruleToCheck = str(page[secondPage] + "|" + page[firstPage])
      if ruleToCheck in rules:
        return False
  return True

def runPartOne():
  allowedScore, partTwo = 0, []
  for page in pages:
    if checkOfAllowed(page):
      allowedScore += int(page[int(len(page)/2 - 0.5)])
    else:
      partTwo.append(page)

  return allowedScore, partTwo

r1, pagesTwo = runPartOne()
print(r1)

def checkOfAllowedTwo(page):
  for firstPage in range(len(page)):
    for secondPage in range(firstPage+1, len(page)):
      ruleToCheck = str(page[secondPage] + "|" + page[firstPage])
      if ruleToCheck in rules:
        #print(ruleToCheck)
        return False, ruleToCheck
  return True, []

def runPartTwo(pagesTwo):
  allowedScore = 0
  for page in pagesTwo:
    pageCheck = page.copy()
    while not checkOfAllowedTwo(pageCheck)[0]:
      valuesToChange = checkOfAllowedTwo(pageCheck)[1].split('|')
      a, b = pageCheck.index(valuesToChange[0]), pageCheck.index(valuesToChange[1])
      pageCheck[b], pageCheck[a] = pageCheck[a], pageCheck[b]
    allowedScore += int(pageCheck[int(len(pageCheck)/2 - 0.5)])

  return allowedScore

print(runPartTwo(pagesTwo))
