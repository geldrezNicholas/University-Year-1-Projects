"""
Function Description:
    The purpose of this function is to check and replace the numbers with the given string.
Parameters:
    x(int): List of integers
    string(string): The word that replaces the integers
    switch(int): The number that is getting switched with the string
Return:
    x: new list of numbers and string 
    counter: the amount things that changed within the list
""" 
def replace(x, string, switch):
    counter = 0
    index = len(x)
    for e in range (0, index):
        if switch == x[e]:
            x.remove(switch)
            x.insert(e,string)
            counter += 1
    return x, counter

flag = True
numbers = []
while flag:
    x = int(input('Number between 1 and 10: '))
    if x > 0 and x < 11:
        numbers.append(x)
    elif(x == -1):
        print(numbers)
        while flag:
            num = input('Enter a number to change [q to quit]')
            if num.lower() == 'q':
                flag = False
            else:
                word = input('with string >>')
                #Call the replace function
                y,c = replace(numbers, word, int(num))
                print(y)
                print(f'It changed {c} time(s).')
    else:
        print('The number must be between 1 and 10!')