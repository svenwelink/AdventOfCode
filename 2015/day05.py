import utils

input = utils.importData("Input/day05.txt")

def ruleOne(string):
    if len([string[x] for x in range(len(string)) if string[x] in ["a", "e", "i", "o", "u"]]) > 2: 
        return True
    return False

def ruleTwo(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True    
    return False

def ruleThree(string):
    for i in range(len(string) - 1):
        if string[i:i+2] in ["ab", "cd", "pq", "xy"]:
            return False
    return True

def niceString(string):
    if ruleOne(string):
        if ruleTwo(string):
            if ruleThree(string):
                return True
    return False
        
def runPartOne(niceStringCount = 0):
    for string in input:
        if niceString(string):
            niceStringCount += 1
    return niceStringCount

print(runPartOne())

def ruleFour(string):
    for i in range(len(string) - 2):
        for j in range(i+2, len(string) - 1):
            if string[i:i+2] == string[j:j+2]:
                return True
    return

def ruleFive(string):
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            return True
    return False

def niceStringTwo(string):
    if ruleFive(string):
        if ruleFour(string):
            return True
    return False

def runPartTwo(niceStringCount = 0):
    for string in input:
        if niceStringTwo(string):
            niceStringCount += 1
    return niceStringCount

print(runPartTwo())
