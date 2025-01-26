import random

list = [[],[],[]]

#random
for e in range(3):
    innerList = []
    for i in range(3):
        innerList.append(random.randint(1,25))
    list[e] = innerList

product = 1
for _ in range(3):
    for value in range(3):
        x = innerList[value]
        product *= x
print(product)