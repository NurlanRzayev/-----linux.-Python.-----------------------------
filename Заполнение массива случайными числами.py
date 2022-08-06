from random import randint

N=10
array=[]

for i in range(N):
    array.append(randint(1,99))

for i in array:
    print(i,end=' ')
    