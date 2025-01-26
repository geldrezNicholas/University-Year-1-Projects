#   COMP 1405 Section C - Assignment 2 Program 1
#    Project Details
#       Name: Nicholas Geldrez
#       Date Created: November 20, 2024
#   External Libraries Used:
#       None

"""
Function Description:
    The purpose of this function is to create matrices based on rows
    and columns and numbers of the rows
Parameters:
    None
Return:
    matrix(List): rows and columns of numbers(list of a lists)
""" 
def createMatrix():
    flag = True
    while flag:
        try:
            rows = int(input("Input number of rows: "))
            cols = int(input("Input number of columns: "))
            flag = False
        except:
            print('Need to be integers!')
    if rows > 0 and cols > 0:
        run = 0
        matrix = []
        while run < rows:
            list = input(f"List the {cols} integers seperated by commas: ")
            seperated = list.split(',')
            try:
                preMatrix = []
                for e in seperated:
                    e = int(e)
                    preMatrix.append(e)
                if len(preMatrix) == cols:
                    matrix.append(preMatrix)
                    run += 1
                else:
                    print(f'Please input {cols} numbers!')
            except:
                print('Make sure they are integers!')
        flag = False
        return matrix
    else:
        print('These need to be positive integers!')

"""
Function Description:
    The purpose of this function is to create matrices based on
Parameters:
    matrix1: list of lists, matrix2: list of lists, matrices from function createMatrix
Return:
    finalMatrix(list of lists): rows and columns of numbers(lists of a list)
""" 
def multipleMatrix(matrix1, matrix2):
    finalMatrix = []
    if len(matrix1[0]) == len(matrix2):
        for rows in range(len(matrix1)):
            finalRow = []
            for cols in range(len(matrix2[0])):
                result = 0
                for j in range(len(matrix2)):
                    result += matrix1[rows][j] * matrix2[j][cols]
                finalRow.append(result)
            finalMatrix.append(finalRow)
        return finalMatrix

"""
Function Description:
    The purpose of this function is to call the previous functions
    ensure that the matrices can multiply, and output them
Parameters:
    None
Return:
    None
""" 
def main():
    flag = True
    while flag:
        matrix1 = createMatrix()
        matrix2 = createMatrix()
        prodMatrix = multipleMatrix(matrix1, matrix2)
        if prodMatrix == None:
            print("These matrices don't work! Please try again.")
            flag = True
        else:
            print('This is the matrix: ')
            for e in prodMatrix:
                print(e)
            flag = False

if __name__ == "__main__":
    main()