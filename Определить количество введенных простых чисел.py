from math import sqrt

num=int(input())

count=0
while num>=2:
    prime_flag=True
    for i in range(2,int(sqrt(num))+1):
        if num%i==0:
            prime_flag=False
            break
    if prime_flag==True:
        count+=1
    num=int(input())

print('Quantity of prime numbers:',count)

#Обрати внимание: если проверить 2 в блоке if num%i==0 , то получим , что 2 составное число , но это не так . Программа очень красиво 
#обходит проверку 2 , т.к. при введении двойки цикл for будет перебирать значения от 2 до 2 , т.е. не произойдет ни одной итерации цикла
#и останется prime_flag==True