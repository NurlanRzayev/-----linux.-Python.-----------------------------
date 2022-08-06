from random import random

N = 5 
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(random() * 10))
    matrix.append(row)

for row in matrix:
    print(row)

sum_main = 0
sum_secondary = 0
for i in range(N):
    sum_main += matrix[i][i]
    sum_secondary += matrix[i][N - i - 1]

print(sum_main)
print(sum_secondary)