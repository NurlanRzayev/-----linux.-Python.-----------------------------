a=abs(int(input()))
sum=0
mult=1
while a>0:
    digit=a%10
    sum+=digit
    mult*=digit
    a//10
print('Sum:',sum)
print('Product:',mult)