#COMP 1405 Section C - Assignment 5 Program 2
#Project Details
    #Name: Nicholas Geldrez
    #Date Created: December 1, 2024
#External Libraries Used:
    #None

def loadData():
    """
    Function Description:
        The purpose of this function is to prompt the user for a CSV file name, 
        read the file contents, and load the recipe data into a list. 
        The first line (header) is removed from the data.
    Parameters:
        None
    Return:
        recipe_data (list): A list of lists where each inner list contains details of a recipe.
    """
    while True:
        fileName = input('Enter the file name: ')
        try:
            with open(fileName, 'r') as file:
                lines = file.readline()
                recipe_data = []
                while lines != "":
                    seperate = lines.strip().split(',')
                    recipe_data.append(seperate)
                    lines = file.readline()
                recipe_data.pop(0)#gets rid of header line('ID,Name,Ingredients,Secret Ingredients')
                return recipe_data
        except FileNotFoundError:
            print('This is not a valid file name!')
            continue
            

def displayList(recipe_data):
    """
    Function Description:
        The purpose of this function is to display the contents of a list of recipes. 
        Each recipe is represented as a list. If the list is empty, a message is displayed.
    Parameters:
        recipe_data (list): A list of lists containing recipe details.
    Return:
        None
    """
    if len(recipe_data) == 0:
        print('List is empty')
    else:
        for e in recipe_data:
            print(e)

def getSecretIngredient(recipe_data):
    """
    Function Description:
        Creates a dictionary of secret ingredients as keys and 
        lists of recipe IDs as values.
    Parameters:
        recipe_data (list): A list of lists containing recipe details.
    Returns:
        secret_ingredient_dict(dictionary): Dictionary of secret ingredients and recipe IDs
    """
    secret_ingredient_dict = {}
    for e in recipe_data:
        if e[3] not in secret_ingredient_dict:
            secret_ingredient_dict[e[3]] = []
    for e in recipe_data:
        secret_ingredient_dict[e[3]].append(e[0])
    return secret_ingredient_dict

def displayDict(secret_ingredient_dict):
    """
    Function Description
        Displays the contents of a dictionary with secret ingredients as keys 
        and recipe IDs as values. Prints a message if the dictionary is empty.
    Parameters:
        secret_ingredient_dict (dict): Dictionary of secret ingredients and recipe IDs.
    Returns:
        None
    """
    if len(secret_ingredient_dict) == 0:
        print('Dictionary is empty')
    else: 
        for e in secret_ingredient_dict:
            print(f'{e}: {secret_ingredient_dict[e]}' )


def main():
    """
    Function Description:
        Loads recipe data, displays the data, puts secret ingredients 
        into a dictionary, and displays the dictionary.
    Parameters:
        None
    Returns:
        None
    """
    recipe_data = loadData()
    displayList(recipe_data)
    secret_ingredient_dict = getSecretIngredient(recipe_data)
    displayDict(secret_ingredient_dict)

if __name__ == '__main__':
    main()