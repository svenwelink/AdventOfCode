# Day 13
print("Day 13")

import numpy as np
import utils

test = utils.importData("TestInput/day13.txt")
data = utils.importData("2023/Input/day13.txt")

def runPartOne(data):
  mirrorPoints = 0
  lastWhiteLineIndex = 0
  for i in range(len(data)):
    if len(data[i].strip()) == 0:
      frame = getFrame(data, lastWhiteLineIndex, i)
      points = getPointsFrame(frame)
      mirrorPoints += points
      lastWhiteLineIndex = i + 1

  # Get last frame
  frame = getFrame(data, lastWhiteLineIndex, len(data))
  points = getPointsFrame(frame)
  mirrorPoints += points
  return(mirrorPoints)

def getFrame(data, firstRow, lastRowPlusOne):
  frame = []
  for i in range(firstRow, lastRowPlusOne):
    row, rowList = data[i].strip(), []
    for j in range(len(row)):
      rowList.append(row[j])
    frame.append(row)
  return(frame)

def getHorizontalMirror(frame):
  for rowId in range(1, len(frame)):
    upperFrame, lowerFrame = frame[:rowId], frame[rowId:len(frame)]
    rowsToCheck = min(len(upperFrame), len(lowerFrame))
  
    if len(upperFrame) < len(lowerFrame):
      lowerPartFrame = lowerFrame[:rowsToCheck]
      lowerPartFrame.reverse()
      if upperFrame == lowerPartFrame:
        return(rowId)
      
    else:
      upperPartFrame = upperFrame[len(upperFrame) - rowsToCheck:]
      lowerFrame.reverse()
      if upperPartFrame == lowerFrame:
        return(rowId)
      
  return(0)

def getPointsFrame(frame):
  horizontalRow = getHorizontalMirror(frame)
  if horizontalRow != 0:
    points = 100 * (horizontalRow)
  else: 
    flippedFrame = transposeList(frame)
    verticalRow = getHorizontalMirror(flippedFrame)
    points = verticalRow 
  return(points)
    
def transposeList(frame):
  transposedFrame = []
  for columnId in range(len(frame[0])):
    newRow = ""
    for rowId in range(len(frame)):
      newRow += frame[rowId][columnId]
    transposedFrame.append(newRow)
  return(transposedFrame)

print("Part one")
print("Test:", runPartOne(test))
print("Result:", runPartOne(data))

# Part 2
# Translate to ones and Zero's 
# Translate from binary number to interger.
# If total difference is 1 

def runPartTwo(data):
  mirrorPoints = 0
  lastWhiteLineIndex = 0
  for i in range(len(data)):
    if len(data[i].strip()) == 0:
      frame = getFrame(data, lastWhiteLineIndex, i)
      points = getPointsFrameTwo(frame)
      mirrorPoints += points
      lastWhiteLineIndex = i + 1

  # Get last frame
  frame = getFrame(data, lastWhiteLineIndex, len(data))
  points = getPointsFrameTwo(frame)
  mirrorPoints += points
  return(mirrorPoints)

def getFrame(data, firstRow, lastRowPlusOne):
  frame = []
  for i in range(firstRow, lastRowPlusOne):
    row, rowList = data[i].strip(), []
    for j in range(len(row)):
      rowList.append(row[j])
    frame.append(row)
  return(frame)

def getHorizontalMirrorTwo(frame):
  for rowId in range(1, len(frame)):
    upperFrame, lowerFrame = frame[:rowId], frame[rowId:len(frame)]
    rowsToCheck = min(len(upperFrame), len(lowerFrame))
  
    if len(upperFrame) < len(lowerFrame):
      lowerPartFrame = lowerFrame[:rowsToCheck]
      lowerPartFrame.reverse()
      if checkFrameOneDiffrentSign(upperFrame, lowerPartFrame):
        return(rowId)
      
    else:
      upperPartFrame = upperFrame[len(upperFrame) - rowsToCheck:]
      lowerFrame.reverse()
      if checkFrameOneDiffrentSign(upperPartFrame, lowerFrame):
        return(rowId)
      
  return(0)

def checkFrameOneDiffrentSign(frameOne, frameTwo):
  difference = 0
  for i in range(len(frameOne)):
    for j in range(len(frameOne[i])):
      if frameOne[i][j] != frameTwo[i][j]:
        difference += 1

  if difference == 1:
    return(True)
  return(False)

def getPointsFrameTwo(frame):
  horizontalRow = getHorizontalMirrorTwo(frame)
  if horizontalRow != 0:
    points = 100 * (horizontalRow)
  else: 
    flippedFrame = transposeList(frame)
    verticalRow = getHorizontalMirrorTwo(flippedFrame)
    points = verticalRow 
  return(points)

print("Part 2")
print("Test", runPartTwo(test))
print("Result:", runPartTwo(data))
