from random import randint , random

print('Range of integers: ')
imin=int(input())
imax=int(input())
n=randint(imin,imax)
print(n)

print('Range of floats: ')
fmin=int(input())
fmax=int(input())
n=random()*(fmax-fmin)+fmin#см. что возвращает random() , умножаем это на длинну диапазона , а потом сдвигаем левую границу на fmin
print('%.3f'%n)