import utils

test = [x.strip() for x in utils.importData("TestInput/day12.txt")]
input = [x.strip() for x in utils.importData("Input/day12.txt")]

for i in test:
    print(i)

class shape:
    def __init__(self, shapeList):
        self.frame = shapeList
        self.length = len(shapeList)
        self.height = len(shapeList)
        self.area = len([point for row in shapeList for point in row if point == "#"])

x = shape([["#", ".", "#"], ["#", ".", "#"], ["#", ".", "#"]])
print(x.frame)
print(x.area)

def prepData(data):
    shapes, boxes = [], []
    for rowId in range(len(data)):
        if data[rowId] == ":"
