n=int(input())

f1=f2=1
print(f1,f2,end=' ')

while n>2:
    f1,f2=f2,f1+f2
    print(f2,end=' ')
    n-=1
print()
