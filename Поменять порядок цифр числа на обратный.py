n1=int(input('An integer: '))
n2=0

while n1>0:
    digit=n1%10
    n1=n1//10
    n2=n2*10#тогда n2+digit будет эквивалентен добавлению цифры в конец числа
    n2=n2+digit

print('Inverse number:',n2)