import utils

test = [x.strip() for x in utils.importData("TestInput/day12.txt")]
input = [x.strip() for x in utils.importData("Input/day12.txt")]

class present:
    def __init__(self, input):
        self.id = int(input[0].strip().strip(":"))
        self.height = len(input) -1 
        self.lenght = len(input[1])
        self.frameString = input[1:]
        self.size = 0
        self.frame = []

    def makeFrameAndCalcSize(self):
        self.frame = []
        for row in self.frameString:
            rowList = []
            for i in range(len(row)):
                if row[i] == "#":
                    rowList.append(1)
                    self.size += 1
                else:
                    rowList.append(0)
            self.frame.append(rowList)

class box:
    def __init__(self, string):
        self.dimensions = string.split(":")[0]
        presentCountString = string.split(":")[1].strip().split(" ")
        self.presentCounts = [int(x) for x in presentCountString]
        self.height = int(self.dimensions.split("x")[0])
        self.length = int(self.dimensions.split("x")[1])

    def calcSpace(self):
        return self.height * self.length

def prepData(data, n_presents = 6, i = 0):
    presents, boxes = [], []

    for id in range(n_presents):
        x = present(data[(id * 5):(id * 5 + 4)])
        x.makeFrameAndCalcSize()
        presents.append(x)

    for id in range(5 * n_presents, len(data)):
        x = box(data[id])
        boxes.append(x)

    return presents, boxes

def presentsFitInBox(presentSizes, boxI:box):
    totalSizeNeeded = sum([count * size for count, size in zip(boxI.presentCounts, presentSizes)])
    if totalSizeNeeded <= boxI.calcSpace():
        return True
    return False

def runPartOne(data, boxCount = 0):
    presents, boxes = prepData(data)
    presentSizes = [x.size for x in presents]
    for boxI in boxes:
        if presentsFitInBox(presentSizes, boxI):
            boxCount += 1
    return boxCount

print(runPartOne(input))
