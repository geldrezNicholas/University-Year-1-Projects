#graph = (vertex, edges)
#vertex = [a,b,c,d]
#edges = [(a,b),(a,b),(a,d),(b,c),(d,b),(d,a),(d,c)]

adj_matrix = [[0,1,1,1],[0,0,1,0],[0,0,0,0],[1,1,1,0]]
adj_list = [[2,3,4],[3],[],[1,2,3]]

def letterFinder(e):
    if e == 0:
        x = 'a'
    elif e == 1:
        x = 'b'
    elif e == 2:
        x = 'c'
    else:
        x = 'd'
    return x

def matrixEdges(matrix):
    for e in range(len(matrix)):
        firstLetter = letterFinder(e)
        if (matrix[e][0] == 1 or matrix[e][1] == 1 or matrix[e][2] == 1 or matrix[e][3] == 1):            
            for i in range(len(matrix)):
                secondLetter = letterFinder(i)              
                if matrix[e][i] == 1:
                    print(f'{firstLetter} -> {secondLetter};', end = '\t')
        else:
            print(f'{firstLetter} has no edges', end = '')
        print()

def listEdges(list):
    for e in range(len(list)):
        firstLetter = letterFinder(e)
        if (len(list[e]) > 0):     
            for i in range(len(list[e])):
                secondLetter = letterFinder(list[e][i]-1)
                print(f'{firstLetter} -> {secondLetter};', end = '\t')
        else:
            print(f'{firstLetter} has no edges', end = '')    
        print()   

def main():
    matrixEdges(adj_matrix)
    print()
    listEdges(adj_list)

if __name__ == main():
    main()
    