import displayCustomer as displayCustomer

def createRecord():
    name = input('What name would you like to add?')
    customerInfo = []
    customerInfo.append(name)
    discount = input('What is the discount type?(G, S, B)')
    customerInfo.append(discount)
    cost = float(input('What is the cost of the order?'))
    customerInfo.append(cost)
    return customerInfo

def main():
    amountOfCust = int(input('How many customers would you like to add?:'))
    customersList = []
    for _ in range(amountOfCust):
        print(f'Customer {_+1}')
        customersList.append(createRecord())
    displayCustomer.printLists(customersList)


if __name__ == "__main__":
    main()