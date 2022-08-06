a=int(input())
b=int(input())

while a!=0 and b!=0:
    if a>b:
        a%=b
    else:
        b%=a

gcd=a+b#одна из переменных содержит 0 , другая НОД
print(gcd)