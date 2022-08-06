from random import random

N = 20
array = []
for i in range(N):
    array.append(int(random() * 100))
array.sort()
print(array)

number = int(input())

low = 0
high = N - 1
while low <= high: # как только левый индекс станет больше на 1 правого, или правый на 1 меньше левого, цикл закончится
    mid = (low + high) // 2
    if number < array[mid]: # если число находится левее середины массива (середины отрезка массива)
        high = mid - 1 # правая граница сдвигается на 1 до середины
    elif number > array[mid]:
        low = mid + 1 # левая граница сдвигается за середину на 1
    else:
        print('ID =', mid)
        break
else: # если выход из цикла произошел не принужденно, т. е. low <= high вернуло False, то сработает эта ветка с else
    print('No the number')