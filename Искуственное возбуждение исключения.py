lst = ['a', 'b', 'c', 'd', 'e', 'f']
letter = input()

if letter in lst:
    print(1)
else:
    raise ValueError('No such letter')