def lcm(a, b):
    m = a * b
    while a != 0 and b != 0: # находим НОД по алгоритму Эвклида
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b) # НОК вычисляется с помощью деления произведения чисел на их НОД

x = int(input('a = '))
y = int(input('b = '))
print('LCM:', lcm(x, y))