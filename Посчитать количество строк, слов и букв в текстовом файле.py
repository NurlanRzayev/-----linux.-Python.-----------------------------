import sys

fname = sys.argv[1] # argv - список аргументов командной строки, argv[0] - имя самого файла-скрипта, argv[1] - первый аргумент
lines = 0
words = 0
letters = 0

for line in open(fname):
    lines += 1
    letters += len(line)

    pos = 'out' # флаг сигнализирующий нахождение за пределами слова
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'

print('Lines:', lines)
print('Words:', words)
print('Letters:', letters)