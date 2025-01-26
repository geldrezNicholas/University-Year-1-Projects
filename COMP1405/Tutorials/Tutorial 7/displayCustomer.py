def printLists(customerList):
    for e in customerList:
        printIndividualList(e)

def printIndividualList(customer):
    if customer[1] == 'B':
        discount = customer[2] * 0.02
        total = customer[2] - discount
        print(f'{customer[0]} has a bronze discount status of 2%, order of ${customer[2]} is discounted ${discount:.2f} for a final total of ${total:.2f}')
    elif customer[1] == 'G':
        discount = customer[2] * 0.1
        total = customer[2] - discount
        print(f'{customer[0]} has a gold discount status of 10%, order of ${customer[2]} is discounted ${discount:.2f} for a final total of ${total:.2f}')
    elif customer[1] == 'S':
        discount = customer[2] * 0.05
        total = customer[2] - discount
        print(f'{customer[0]} has a silver discount status of 5%, order of ${customer[2]} is discounted ${discount:.2f} for a final total of ${total:.2f}')
    print()

customerRecords = [['Sean Benjamin', 'B', 30.22],['Yanan Mao', 'G', 40.22], ['Charlie Brown', 'S', 22.30],
['Snoopy Dog', 'G', 69.33], ['Woodstock Bird', 'S', 25.00]]
    
printLists(customerRecords)