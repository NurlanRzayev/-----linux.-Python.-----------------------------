def disp_binary(u):
    
    t=128                        #128=10000000 64=01000000 32=00100000 ... 1=00000001
    while t>0:                   #можно while t:
        if u&t:
            print('1',end='')
        else:
            print('0',end='')
        t=t//2                   #можно t=t>>1
    print()

disp_binary(35)
disp_binary(11)

def move():
    
    i=1
    for j in range(8):
        disp_binary(i)
        i=i<<1
    print()
    for j in range(8):
        i=i>>1                  #это нужно обязательно писать до вызова disp_binary , т.к. после последней итерации предыдущего цикла i имеет значение 256 которое не было передано в disp_binary , отсюда если мы поменяем строки местами во втором цикле то после первой итерации получим 100000000 ( 8 нулей )
        disp_binary(i)


print()
move()