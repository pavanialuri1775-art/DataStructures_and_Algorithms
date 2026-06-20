#taking matrix input from the user
mat=[]
rows=int(input())
columns=int(input())
for i in range(rows):
    row=[]
    for j in range(columns):
        val=int(input("enter a value:"))
        row.append(val)
    mat.append(row)
print(mat)

#Print Matrix Elements Row-wise
matrix=[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
rows=len(matrix)
columns=len(matrix[0])
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j],end=" ")
        
#Print Matrix Elements Column-wise
matrix=[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
rows=len(matrix)
columns=len(matrix[0])
for j in range(columns):
    for i in range(rows):
        print(matrix[i][j],end=" ")#1 4 7 2 5 8 3 6 9 
        
        
#Find Sum of diagonal elements  in Matrix
matrix=[
 [1,2],
 [3,4]
]
sum=0
n=len(matrix)
for i in range(n):
    sum+=matrix[i][i]
print(sum)

#sum of all elements in a matrix
matrix=[
 [1,2],
 [3,4]
]
total=0
rows=len(matrix)
columns=len(matrix[0])
for i in range(rows):
    for j in range(columns):
        total+=matrix[i][j]
print(total)

#Find Largest Element in Matrix
matrix=[
[10,5,8],
[2,20,3]
]
max_element=matrix[0][0]
rows=len(matrix)
columns=len(matrix[0])
for i in range(rows):
    for j in range(columns):
        if matrix[i][j]>max_element:
            max_element=matrix[i][j]
print(max_element)

#Count Even and Odd Numbers in Matrix
matrix=[
 [1,2,3],
 [4,5,6]
]
even_count=0
odd_count=0
rows=len(matrix)
columns=len(matrix[0])
for i in range(rows):
    for j in range(columns):
        if matrix[i][j]%2==0:
            even_count+=1
        else:
            odd_count+=1
print("even count:",even_count)
print("odd count:",odd_count)
        