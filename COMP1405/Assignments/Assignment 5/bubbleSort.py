#COMP 1405 Section C - Assignment 5 Program 3
#Project Details
    #Name: Nicholas Geldrez
    #Date Created: December 2, 2024
#External Libraries Used:
    #None

def separate_numbers(original):
    """
    Function Description:
        The purpose of this function is to separate the list into two lists,
        one being non-negative numbers, the other being negative numbers
    Parameters:
        original(list): the list in which we are separating in negative and 
        non-negative numbers
    Return:
        non_negatives(list): list of non-negative numbers
        negative(list): list of negative numbers
    """
    non_negatives =[]
    negatives = []
    for e in original:
        if e >= 0:
            non_negatives.append(e)
        else:
            negatives.append(e)
    return non_negatives, negatives

def bubble_sort(aList, ascending):
    """ 
    Function Description:
        The purpose of this function is to sort the list using the bubble sort algorithm
        in either ascending or descending order based on the value of the ascending parameter.
    Parameters:
        aList(list): The list of numbers to be sorted
        ascending(boolean): Whether the function separates it ascending or descending
    Return:
        aList(list): Sorted list of numbers
    """
    if ascending:
        for e in range(len(aList)):
            swapped = False
            for f in range(0, len(aList) - e - 1):
                if aList[f] > aList[f + 1]:
                    temp = aList[f]           
                    aList[f] = aList[f + 1]       
                    aList[f + 1] = temp 
                    swapped = True
            if not swapped:
                break
    else: 
        for e in range(len(aList)):
            swapped = False
            for f in range(0, len(aList) - e - 1):
                if aList[f] < aList[f + 1]:
                    temp = aList[f]           
                    aList[f] = aList[f + 1]       
                    aList[f + 1] = temp 
                    swapped = True
            if not swapped:
                break
    return aList

def main():
    """
    Function Description:
        The purpose of this function is to call functions and print results
    Parameters:
        None
    Return:
        None
    """
    integerList = [12, -7, 3, -45, 22, 8, 0, -13, 19, -21, 5,
                    -9, -11, 15, 30, -33, -4, 7, 25, -2]
    lists = separate_numbers(integerList)
    non_negative = lists[0]
    negative = lists[1]
    print(f'Original List: {integerList}')
    print(f'Non-Negative ascending: {bubble_sort(non_negative, True)}')
    print(f'Non-Negative descending: {bubble_sort(non_negative, False)}')
    print(f'Negative ascending: {bubble_sort(negative, True)}')
    print(f'Negative descending: {bubble_sort(negative, False)}')

if __name__ == '__main__':
    main()