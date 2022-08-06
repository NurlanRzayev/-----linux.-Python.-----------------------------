n1=input('Binary n1: ')
n2=input('Binary n2: ')
print()

n1=int(n1,2)#перевод введенной строки из двоичной системы в десятичную
n2=int(n2,2)

bit_or=n1|n2
bit_and=n1&n2
bit_xor=n1^n2

bit_or=bin(bit_or)
bit_and=bin(bit_and)
bit_xor=bin(bit_xor)

print('n1: %10s'%bin(n1))#функция bin() возвращает строку , которая содержит перевод десятисного числа в двоичную сист. счис.
print('n2: %10s'%bin(n2))
print('    ____________')
print(' OR: %10s'%bit_or)
print('AND: %10s'%bit_and)
print('XOR: %10s'%bit_xor)