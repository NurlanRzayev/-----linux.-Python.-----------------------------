from random import randint

N=7
a=[]

for i in range(N):
    a.append(randint(0,100))
    print(a[i],end=' ')
print()

maximum=0#минимальный макс. , он равен истинному макс. в том случае если все эл. списка равны нулю , при большем значении этой переменной программа не всегда давала бы верный результат
minimum=100#максимальный мин. , он равен истинному мин. в том случае если все эл. списка равны ста ...
for x in a:
    if x>maximum:
        maximum=x
    if x<minimum:
        minimum=x

print('Maximum=',maximum)
print('Minimum=',minimum)