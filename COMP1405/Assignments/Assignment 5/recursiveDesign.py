#COMP 1405 Section C - Assignment 5 Program 1
#Project Details
    #Name: Nicholas Geldrez
    #Date Created: December 1, 2024
#External Libraries Used:
    #None

def sum_of_evens_non_recursive(aList):
    """
    Function Description:
        The purpose of this function  is to take the sum of all
        even numbers, non-recursively
    Parameters:
        aList(list): list of numbers
    Return:
        sum(int): sum of even numbers
    """ 
    sum = 0
    for e in aList:
        if e % 2 == 0:
            sum+=e
    return sum

def sum_of_odds_non_recursive(aList):
    """
    Function Description:
        The purpose of this function  is to take the sum of all
        odd numbers, non-recursively
    Parameters:
        aList(list): list of numbers
    Return:
        sum(int): sum of odd numbers
    """ 
    sum = 0
    for e in aList:
        if e % 2 != 0:
            sum+=e
    return sum

def sum_of_evens_recursive(aList):
    """
    Function Description:
        The purpose of this function is to calculate the sum of all
        even numbers in a list, recursively.
    Parameters:
        aList (list): A list of numbers.
    Return:
        int: The sum of all even numbers in the list.
        None: If the input list is empty.
    """
    if len(aList) == 0:
        return 0
    elif aList[0] % 2 == 0:
        return aList[0] + sum_of_evens_recursive(aList[1:])
    else:
        return sum_of_evens_recursive(aList[1:])

def sum_of_odds_recursive(aList):
    """
    Function Description:
        The purpose of this function is to calculate the sum of all
        odd numbers in a list, recursively.
    Parameters:
        aList (list): A list of numbers.
    Return:
        int: The sum of all odd numbers in the list.
        None: If the input list is empty.
    """
    if len(aList) == 0:
        return 0
    elif aList[0] % 2 != 0:
        return aList[0] + sum_of_odds_recursive(aList[1:])
    else:
        return sum_of_odds_recursive(aList[1:])

def main():
    """
    Function Description:
        The purpose of this function is to allow the user to input integers, 
        call functions to get the sum of even and odd numbers using both recursive and non-recursive methods, 
        and display the results. The user can quit the program by entering 'quit'.
    Parameters:
        None
    Return:
        None
    """
    flag = True
    while flag:
        numList = []
        while flag:
            number = input('Enter one number!: ')
            if number.lower() == 'quit':
                flag = False
            else:
                try:
                    numList.append(int(number))
                except:
                    print('Enter a number to add to list or "quit" to exit: ')
        print(f'Even non-recursive: {sum_of_evens_non_recursive(numList)}')
        print(f'Odd non-recursive: {sum_of_odds_non_recursive(numList)}')
        print(f'Even recursive: {sum_of_evens_recursive(numList)}')
        print(f'Odd recursive: {sum_of_odds_recursive(numList)}')
        x = input('Do you want to continue(enter "quit" to close program)?:')
        if x.lower() == 'quit':
            flag = False
        else:
            flag = True

if __name__ == '__main__':
    main()
