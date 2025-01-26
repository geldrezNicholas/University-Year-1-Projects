#   COMP 1405 Section C - Assignment 2 Program 2
#    Project Details
#       Name: Nicholas Geldrez
#       Date Created: October 12, 2024
#   External Libraries Used:
#       None

def runAgain(answer):
    """
    Function Description:
        The purpose of this function is to reset and/or continue the program
    Parameters:
        answer (string): The string in which the user decides to continue or stop the program
    Return:
        boolean: boolean to continue or stop loop
    """ 
    numbers.clear()
    if (answer.lower() == 'yes'):
        flag = True
    elif (answer.lower() == 'no'):
        flag = False      
    return flag

flag = True
numbers = []
while flag:
    start = int(input('When do you want to start(3 digits): '))
    end = int(input('When do you want to end(3 digits): '))
    if (start >= 100 and start <= 999) and (end >= 100 and end <= 999): #check for 3 digits
        for i in range(start, end+1): 
            #Seperating the 3 digits
            digit3 = i % 10
            digit12 = i // 10
            digit1 = digit12 // 10
            digit2 = digit12 % 10
            if ((digit1**3 + digit2**3 + digit3**3) == i): #if all the cubed digits add up to the number
                numbers.append(i)
        print(f"The narcissistic numbers in range are: {numbers}")
        run = input("Say 'yes' to run again or 'no' to stop: ")
        #Call the runAgain function and set flag as its return 
        flag = runAgain(run)   
    else:
        print('This is not 3 digits.')
        run = input("Say 'yes' to run again or 'no' to stop: ")
        #Call the runAgain function and set flag as its return 
        flag = runAgain(run)          