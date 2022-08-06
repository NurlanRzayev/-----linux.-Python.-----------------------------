from random import randint

N=10
A=[]
sum=0
for i in range(N):
    A.append(randint(0,9))
    print(A[i],end=' ')
    sum+=A[i]
print()

average=sum/N
print('The average: %.2f'%average)

for x in A:
    if x>average:
        print(x,end=' ')
        