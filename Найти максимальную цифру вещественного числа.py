from random import random

num=round(random()*1000,3)
print(num)

str_num=str(num)
max_digit=-1
for i in range(len(str_num)):
    if str_num[i]=='.':
        continue
    elif max_digit<int(str_num[i]):
        max_digit=int(str_num[i])
print(max_digit)