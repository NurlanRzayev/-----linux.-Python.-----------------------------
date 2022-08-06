from random import randint

N=7

a=[]
for i in range(N):
    a.append(randint(1,20))

print(a)

for i in range(N-1):      #см. тетрадь
    for j in range(N-i-1):
        if a[j]>a[j+1]:
            b=a[j]
            a[j]=a[j+1]
            a[j+1]=b

print(a)