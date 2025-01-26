#   COMP 1405 Section C - Assignment 2 Program 1
#    Project Details
#       Name: Nicholas Geldrez
#       Date Created: November 20, 2024
#   External Libraries Used:
#       None

"""
Function Description:
    The purpose of this function is to create a list of words without non-letter characters
Parameters:
    para (str): The paragraph where the words are taken from
Return:
    list: list of new words
""" 
def prepText(para):
    lower = para.lower()
    splitPara = lower.split()
    newWords = []
    for e in splitPara:
        letters = list(e) 
        newLetters = []
        for i in letters:
            if i >= 'a' and i <= 'z':
                newLetters.append(i)
        newWords.append(''.join(newLetters))
    return newWords

"""
Function Description:
    The purpose of this function is to create a dictionary and 
    insert the words as values based on their first letter(keys)
Parameters:
    words (list): List of words taken from the paragraph
Return:
    dictionary: dictionary of letters organized by their first letters(keys)
""" 
def createDict(words):
    dictionary = {}
    for i in range(97,123):
        dictionary[chr(i)] = []
    for e in words:
        dictionary[e[:1]].append(e)
    return dictionary

"""
Function Description:
    The purpose of the function is to call previous functions and print the dictionary
Parameters:
    None
Return:
    None
""" 
def main():
    paragraph = input('Type anything you want!: ')
    words = prepText(paragraph)
    print(createDict(words))

if __name__ == '__main__':
    main()