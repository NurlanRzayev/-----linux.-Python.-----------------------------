first=input('The first: ')
last=input('The last: ')

while first<=last:#first будет счетчиком и выводимой буквой , это ясно по условию цикла
    print(first,end=' ')
    first=chr(ord(first)+1)