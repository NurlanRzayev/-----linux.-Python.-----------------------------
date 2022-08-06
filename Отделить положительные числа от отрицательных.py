from random import random

a=[]
for i in range(7):
    n=int(random()*20)-10#эквивалентно int(random()*20-10) , это диапозон от -10 до 10 не вкл. , целых чисел
    a.append(n)
print(a)

neg=[]
pos=[]
for x in a:
    if x<0:
        neg.append(x)
    elif x>0:
        pos.append(x)
print(neg)
print(pos)

