from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % 2 == 0:
            return False # после того как срабатывает первый return происходит выход из функции
        i += 1
    return True

for i in range(3):
    num = int(input())
    print(is_prime(num))
    