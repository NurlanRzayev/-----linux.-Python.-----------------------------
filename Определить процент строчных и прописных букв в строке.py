string=input()
length=len(string)
lower=upper=0

for i in string:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1

per_lower=lower/length*100
per_upper=upper/length*100
print('Lower: %.2f%%'%per_lower)#чтобы экранировать знак процента и python не воспринимал его как начало паттерна, нужно написать его 2 раза
print('Upper: %.2f%%'%per_upper)