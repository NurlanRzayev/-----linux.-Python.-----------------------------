n=int(input())

factorial=1
while n>1:#здесь счетчиком является введенное число
    factorial*=n
    n-=1

print(factorial)