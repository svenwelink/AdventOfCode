import utils

df = utils.importData()

# Part 1
x, y = [], []
for i in range(len(df)):
    values = df[i].split()
    x.append(int(values[0]))
    y.append(int(values[1]))

x.sort()
y.sort()

totalDiff = 0
for i in range(len(x)):
    totalDiff += abs(y[i] - x[i])

print(totalDiff)

# Part 2
total = 0
for i in range(len(x)):
    countY = list(filter(lambda a: a == x[i], y))
    total += x[i] * len(countY)

print(total)
