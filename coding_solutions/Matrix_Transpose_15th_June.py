# Program to transpose a matrix using a nested loop

X = [[10,6],
    [2 ,4],
    [6 ,8]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)