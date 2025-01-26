#1

menu = ['Ice Cream', 3.67, 2, 'Donuts', 2.50, 6, 'Roll', 7.89, 3, 'Pizza', 13.45, 5, 
        'Fish and Chips', 15.20, 23, 'Poutine', 8.51, 13, 'Tacos', 3.00, 19]

#2

#a
foodItems = menu[::3]
prices = menu[1::3]
quantities = menu[2::3]

#b

total = 0
for e in foodItems:
    total += len(e)
mean = total/7

#c

updatePrice = []
num = 0
for i in prices:
    updatePrice.append(round(i * quantities[num], 2))
    num += 1

#d.

updateQ = []
for x in quantities:
    updateQ.append(chr(x+64))

#3.

print(f'The mean length of the item names is {int(mean)}')
print(f'Menu Order Summary:(Food Name: Price, Quantity)')
num3 = 0
for d in foodItems:
    print(f'{d}: {updatePrice[num3]} , {updateQ[num3]}')
    num3 += 1