import utils

df_input = utils.importData()
df = [x.strip() for x in df_input]

def checkXmasAround(x, y):
  score = 0
  #Right
  if y+4 <= len(df[x]):
    if df[x][y:y+4] == 'XMAS':
       score += 1
  #Left
  if y-3 >= 0:
    if df[x][y] + df[x][y-1] + df[x][y-2] + df[x][y-3] == 'XMAS':
       score += 1
  #Up
  if x-3 >= 0:
    if df[x][y] + df[x-1][y] + df[x-2][y] + df[x-3][y]  == 'XMAS':
       score += 1
  #Down
  if x+4 <= len(df):
    if df[x][y] + df[x+1][y] + df[x+2][y] + df[x+3][y]  == 'XMAS':
       score += 1
  #UpLeft
  if x-3 >= 0 and y-3 >= 0:
    if df[x][y] + df[x-1][y-1] + df[x-2][y-2] + df[x-3][y-3]  == 'XMAS':
       score += 1
  #UpRight
  if x-3 >= 0 and y+4 <= len(df[x]):
    if df[x][y] + df[x-1][y+1] + df[x-2][y+2] + df[x-3][y+3]  == 'XMAS':
       score += 1
  #DownRight
  if x+4 <= len(df) and y+4 <= len(df[x]):
    if df[x][y] + df[x+1][y+1] + df[x+2][y+2] + df[x+3][y+3]  == 'XMAS':
       score += 1
  #DownLeft
  if x+4 <= len(df) and y-3 >= 0:
    if df[x][y] + df[x+1][y-1] + df[x+2][y-2] + df[x+3][y-3]  == 'XMAS':
       score += 1
  return score

def runPartOne():
  xmasCount = 0

  for x in range(len(df)):
    for y in range(len(df[x])):
      if df[x][y] == 'X':
        xmasCount += checkXmasAround(x, y)

  return xmasCount

print(runPartOne())

def checkXmasAroundTwo(x,y):
  if df[x-1][y-1] == "M" and df[x-1][y+1] == "M" and df[x+1][y-1] == "S" and df[x+1][y+1] == "S":
    return True
  elif df[x-1][y-1] == "S" and df[x-1][y+1] == "M" and df[x+1][y-1] == "S" and df[x+1][y+1] == "M":
    return True
  elif df[x-1][y-1] == "S" and df[x-1][y+1] == "S" and df[x+1][y-1] == "M" and df[x+1][y+1] == "M":
    return True
  elif df[x-1][y-1] == "M" and df[x-1][y+1] == "S" and df[x+1][y-1] == "M" and df[x+1][y+1] == "S":
    return True
  return False


def runPartTwo():
  xmasCount = 0

  for x in range(1, len(df) - 1):
    for y in range(1, len(df[x]) - 1):
      if df[x][y] == 'A':
        if checkXmasAroundTwo(x, y):
          xmasCount += 1

  return xmasCount

print(runPartTwo())
