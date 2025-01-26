"""
Function Description:
    The purpose of this function is to check if the inputed height is within the range
Parameters:
    num (int): The height of the tree 
Return:
    None
""" 
def checkError(num):
    if num < 2:
        print("Looks like we've got a baby tree here not quite ready for Christmas cheer.")
    elif num > 10:
        print("Whoa, that tree is too big for my cozy living room. Let's find one that fits just right.")
    else:
        #Call the generateTree function and generates the tree based on the height
        generateTree(int(x))

"""
Function Description:
    The purpose of this function is to check generate and print out the tree based on the given height
Parameters:
    height (int): The height of the tree
Return:
    None
""" 
def generateTree(height):
    for e in range(0, height):
        stars = (2 * e) + 1
        spaces = height - e - 1
        print(' '*spaces, '*'*stars)
    print(' '*(height-1), '|')

x = input('What height is your tree or type quite to stop?')
while x.lower() != 'quit':
    #Call the checkError function and checks the height is within range
    checkError(int(x))
    x = input('What height is your tree or type quite to stop?')