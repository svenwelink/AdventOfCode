import hashlib

input = "iwrupvqb"

def getLeftXOfMD5(input, intergers):
    return hashlib.md5(input.encode()).hexdigest()[:intergers]

def runPartOne(xValue = 1, notFound = True):
    while notFound:
        if getLeftXOfMD5(input + str(xValue), 5) == "00000":
            return xValue
        xValue += 1

print(runPartOne())

def runPartTwo(xValue = 346386, notFound = True):
    while notFound:
        if getLeftXOfMD5(input + str(xValue), 6) == "000000":
            return xValue
        xValue += 1

print(runPartTwo())
