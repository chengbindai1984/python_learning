import random
import math
import copy
# math.sqrt(3)

number1 = random.randint(1, 10000)

number2 = random.randint(1, 10000)

if number1 > number2:
    startNumber = number2
    endNumber = number1
else:
    startNumber = number1
    endNumber = number2
# math.pow(number,2)

print(startNumber, endNumber)

sqrList = []

for i in range(1, 100):
    sqrNumber = math.pow(i, 2)
    sqrList.append(sqrNumber)
    # print(sqrList)

# print(sqrList)

newSqrList = copy.deepcopy(sqrList)
newSqrList.append(startNumber)
newSqrList.append(endNumber)
newSqrList.sort()

# print(newSqrList)

newSqrList.index(startNumber)

newSqrList.index(endNumber)

answer = newSqrList.index(endNumber) - newSqrList.index(startNumber)-1

print(answer)
