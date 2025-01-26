sales = [["customer1", "bread", 5], ["customer2", "bread", 4.5], ["customer1", "egg", 6.75],
["customer2","milk", 4.35], ["customer3","egg", 3.6], ["customer4", "bread", 4.5],["customer1", "milk", 4.35], 
["customer2", "egg", 3.6], ["customer4", "milk", 4.35]]

def listToDictionary(aList):
    d = {}
    for specificList in aList:
        customer = specificList[0]
        if customer not in d:
            d[customer] = [[], 0]

    for specificList in aList:
        customer = specificList[0]
        item = specificList[1]
        d[customer][0].append(item)

    for specificList in aList:
        customer = specificList[0]
        price = specificList[2]
        d[customer][1] += price
    print(d)
    return d

def display(aDictionary):
    for customer in aDictionary:
        print(f'{customer} : {aDictionary[customer]}')

def main():
    d = listToDictionary(sales)
    display(d)

if __name__ == main():
    main()
    