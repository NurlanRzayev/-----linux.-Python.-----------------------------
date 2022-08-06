from random import random

a=[]
for i in range(7):
    n=int(random()*100)
    a.append(n)
print(a)

even=0
odd=0
for x in a:
    if x%2==0:
        even+=1
    else:
        odd+=1
print('Even:',even)
print('Odd:',odd)
