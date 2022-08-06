import random

arr=[]
for i in range(30):
    x=int(random.random()*100)
    arr.append(x)
    print('%3d'%x,end='')
    if (i+1)%5==0:
        print()

minimum=int(input('Min: '))
maximum=int(input('Max: '))

qty=0
for i in arr:
    if minimum<=i<=maximum:
        qty+=1
print(qty)