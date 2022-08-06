from random import random

matrix = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(int(random() * 10))
    matrix.append(row)
for row in matrix:
    print(row)

max_row = 0
id_row = 0
i = 0
for row in matrix:
    if sum(row) > max_row:
        max_row = sum(row)
        id_row = i
    i += 1
print(id_row, '-', max_row)

max_col = 0
id_col = 0
for i in range(5):
    col_sum = 0
    for j in range(5):
        col_sum += matrix[j][i]
    if col_sum > max_col:
        max_col = col_sum
        id_col = i
print(id_col, '-', max_col)