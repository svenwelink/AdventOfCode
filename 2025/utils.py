import utils

test = utils.importData("TestInput/day06.txt")
input = utils.importData("Input/day06.txt")

def prepData(data):
    data = [x.strip().split(" ") for x in data]
    for x in range(len(data)):
        if x == len(data) - 1:
            data[x] = [y for y in data[x] if y != ""]
        else:
            data[x] = [y for y in data[x] if y != ""]
    data = utils.transposeList(data)
    return data

def mult(inst, mult = 1):
    for i in range(len(inst) -1 ):
        mult = int(mult) * int(inst[i])
    return mult

def summation(inst, xSum = 0):
    for i in range(len(inst) -1 ):
        xSum += int(inst[i])
    return xSum

def calulateSumOfPrepedData(prepedData, totalSum = 0):
    for eqaution in prepedData:
        if eqaution[-1] == "*":
            totalSum += mult(eqaution)
        elif eqaution[-1] == "+":
            totalSum += summation(eqaution)
    return totalSum

def runPartOne(data):
    data = prepData(data)
    totalSum = calulateSumOfPrepedData(data)
    return totalSum

print(runPartOne(input))

def prepPartTwo(data, newData = [], newRow = []):
    for i in range(len(data[0]) - 1):
        newString = ""
        for j in range(len(data)):
            try:
                if data[j][i] == "*" or data[j][i] == "+":
                    sign = data[j][i]
                else: newString += data[j][i]
            except: # some list are longer
                pass

        if newString == " " * len(data):
            newRow.append(sign)
            newData.append(newRow)
            newRow = []
        else:
            newRow.append(int(newString.strip(" ")))
    
    # add the last row
    newRow.append(sign)
    newData.append(newRow)
    return newData

def runPartTwo(data):
    data = prepPartTwo(data)
    totalSum = calulateSumOfPrepedData(data)
    return totalSum

print(runPartTwo(input))
