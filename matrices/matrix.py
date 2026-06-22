#1  Matrix:A matrix is a collection of elements arranged in rows and columns.
#In python we represent a matrix using list of lists.
#example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Number of rows = 3
#Number of columns = 3
#Size = 3*3

#travese a matrix
#row wise traversal:Reading top to bottom
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])
        
#Column-wise traversal:Reading top to bottom
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rows = len(matrix)
columns = len(matrix[0])
for j in range(columns):
    for i in range(rows):
        print(matrix[i][j],end=" ")
        
#Diagonal traversal:The main diagonal goes from top-left to bottom-right.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n=len(matrix)
for i in range(n):
    print(matrix[i][i])
    
#Anti-Diagonal Traversal:The anti-diagonal goes from top-right to bottom-left.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n=len(matrix)
for i in range(n):
    print([i][n-1-i])
    
#Traversing All Diagonals
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rows=len(matrix)
columns=len(matrix[0])
diagonal={}
for i in range(rows):
    for j in range(columns):
        if i+j not in diagonal:
            diagonal[i+j]=[]
        diagonal[i+j].append(matrix[i][j])
for key in diagonal:
    print(diagonal[key])