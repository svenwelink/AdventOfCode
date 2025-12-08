import utils
from math import sqrt
from operator import attrgetter

test = utils.importData("TestInput/day08.txt")
input = utils.importData("Input/day08.txt")

class juctionBox:
    def __init__(self, coords, id):
        self.xValue = int(coords[0])
        self.yValue = int(coords[1])
        self.zValue = int(coords[2])
        self.id = id 

class boxConnection:
    def __init__(self, box1:juctionBox, box2:juctionBox):
        self.id1 = box1.id
        self.id2 = box2.id
        self.dist = calculateDist(box1, box2)

    def reverseBox(self):
        self.id1, self.id2 = self.id2, self.id1
        return self

def calculateDist(box1:juctionBox, box2:juctionBox):
    dist = sqrt(abs(box1.xValue - box2.xValue)**2 + abs(box1.yValue - box2.yValue)**2 + abs(box1.zValue - box2.zValue)**2)
    return dist

def createJunctionBoxList(data):
    dataList = []
    for id in range(len(data)):
        boxList = data[id].strip().split(",")
        dataList.append(juctionBox(boxList, id))

    return dataList

def findConnection(connection:boxConnection, connectBoxes, reverse = True):
    for circuit in connectBoxes:
        if connection.id1 in circuit:
            if connection.id2 in circuit:
                return connectBoxes
            else:
                # if exists in another circuit
                for circuit2 in connectBoxes:
                    if connection.id2 in circuit2:
                        for id in circuit2:
                            circuit.append(id)

                        connectBoxes.remove(circuit2)
                        return connectBoxes
                    
                # no other circuit
                circuit.append(connection.id2)
            return connectBoxes
    
    if reverse:
        connectBoxes = findConnection(connection.reverseBox(), connectBoxes, reverse = False)
    else:
        connectBoxes.append([connection.id1, connection.id2])
    return connectBoxes

def getAllDistinces(boxList):
    distList = []
    for i in range(len(boxList)):
        for j in range(i + 1, len(boxList)):
            distList.append(boxConnection(boxList[i], boxList[j]))
    distList = sorted(distList, key=attrgetter("dist"))
    return distList

def runPartOne(data, connections, circuits = []):
    boxList = createJunctionBoxList(data)
    distList = getAllDistinces(boxList)
    for round in range(connections):
        circuits = findConnection(distList[round], circuits)

    circuitLengths = sorted([len(x) for x in circuits], reverse = True)
    return circuitLengths[0] * circuitLengths[1] * circuitLengths[2]

print(runPartOne(input, 1000))

def runPartTwo(data, circuits = []):
    boxList = createJunctionBoxList(data)
    distList = getAllDistinces(boxList)
    round, notFinished = 0, True
    while notFinished:
        circuits = findConnection(distList[round], circuits)
        if notFinished:
            if len(circuits) == 1 and round > 1:
                if len(circuits[0]) == len(data):
                    notFinished = False
        round += 1

    orgDistanceList = getAllDistinces(boxList)
    lastIds = [orgDistanceList[round - 1].id1, orgDistanceList[round - 1].id2]
    xValue1, xValue2 = data[lastIds[0]].strip().split(",")[0], data[lastIds[1]].strip().split(",")[0]
    return int(xValue1) * int(xValue2)

print(runPartTwo(input))
