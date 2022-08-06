from random import random

N = 6
M = 5
matrix = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(int(random() * 40) + 10)
    matrix.append(row)

for row in matrix:
    print(row)

item = int(input('Number range(10, 50): '))

print('Rows index:', end=' ')
for i in range(N):
    if item in matrix[i]:
        print(i, end=' ')
print()
print('Columns index:', end=' ')
for j in range(M):
    for i in range(N):
        if item == matrix[i][j]:
            print(j, end=' ')
            break # если в столбце имеется уже искомый элемент, то индекс столбца будет выведен, то есть дальше перебирать элементы столбца не нужно, иначе если в столбце окажется несколько одинаковых элементов, соответствующих искомому, то номер столбца будет выведен несколько раз