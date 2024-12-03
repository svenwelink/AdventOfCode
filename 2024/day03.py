import re
import utils

df = utils.importData('')

sum = 0
for line in df:
  values = re.findall("mul[(]([1-9]|[1-9][0-9]|[1-9][0-9][0-9]),([1-9]|[1-9][0-9]|[1-9][0-9][0-9])[)]", line)

  for pair in values:
    pairValues = [int(i) for i in pair]
    sum += pairValues[0] * pairValues[1]

# Part 1
print(sum)

# Part 2
totalString = ""
for line in df:
  totalString += line

values = re.findall("(mul[(]([1-9]|[1-9][0-9]|[1-9][0-9][0-9]),([1-9]|[1-9][0-9]|[1-9][0-9][0-9])[)])|(do[(][)])|(don't[(][)])", totalString)

enabeld = True
sum  = 0

for pair in values:
  if pair[3] == "do()":
    enabeld = True
  elif pair[4] == "don't()":
    enabeld = False
  elif enabeld:
    pairValues = [i for i in pair]
    sum += int(pairValues[1]) * int(pairValues[2])

print(sum)
