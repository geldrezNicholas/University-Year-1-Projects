#   COMP 1405 Section C - Assignment 2 Program 1
#    Project Details
#       Name: Nicholas Geldrez
#       Date Created: October 11, 2024
#   External Libraries Used:
#       None

def findDivisors(x):
    """
    Function Description:
        The purpose of this function is to find the divisors of a given number
    Parameters:
        x (int): The number whos divisors we are finding
    Return:
        list: list of divisors
    """ 
    divisors = []
    for i in range(1, x+1):
        if (x%i == 0):
            divisors.append(i)
    return divisors

a = int(input("Pick any number: "))
print(f'The divisors are: {findDivisors(a)}')