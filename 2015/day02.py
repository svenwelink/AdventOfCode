import utils

input = utils.importData("Input/day02.txt")
input = [box.strip().split("x") for box in input]

def getSizes(sidesLengths):
    sizes, nSides = [], len(sidesLengths)
    for i in range(nSides):
        for j in range(i+1, nSides):
            sizes.append(int(sidesLengths[i]) * int(sidesLengths[j]))

    return sizes

def getWrappingPaperSize(instruction):
    sizes = getSizes(instruction)
    return sum(sizes) * 2 + min(sizes)

def runPartOne(data, totalSum = 0):
    for boxDimension in data:
        totalSum += getWrappingPaperSize(boxDimension)
    return totalSum

print(runPartOne(input))

def getRibonSize(lengths):
    lengths = [int(value) for value in lengths]
    lengths.sort()
    return (lengths[0] + lengths[1]) * 2 + (lengths[0]*lengths[1]*lengths[2])

def runPartTwo(data, totalSum = 0):
    for boxDimension in data:
        totalSum += getRibonSize(boxDimension)
    return totalSum

print(runPartTwo(input))
