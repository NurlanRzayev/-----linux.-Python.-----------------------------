a = b = ''
while type(a) != int or type(b) != int:#цикл завершится только тогда, когда обе переменные будут содержать целые числа
    a = input()
    b = input()
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print('Input integers.')

try:
    c = a / b
except ZeroDivisionError:
    print('Cannot be divided by zero.')
else:
    print(c)
