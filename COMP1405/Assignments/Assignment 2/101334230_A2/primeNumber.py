#   COMP 1405 Section C - Assignment 2 Program 2
#    Project Details
#       Name: Nicholas Geldrez
#       Date Created: October 12, 2024
#   External Libraries Used:
#       random

import random

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

a = random.randint(1,30)
#Call the findDivisors function and checks if the number has 2 divisors
if (len(findDivisors(a)) == 2):
    print(f'{a} is a prime number')
else:
    print(f'{a} is not a prime number')