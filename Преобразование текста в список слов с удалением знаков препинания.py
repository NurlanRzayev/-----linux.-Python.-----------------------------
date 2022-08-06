string = input('Write down a text:\n')

signs = ['.', ',', ':', ';', '?', '!', '(', ')']
words = string.split()

i = 0
for word in words:
    if word[-1] in signs: # если слово заканчивается на знак препинания
        words[i] = word[:-1]
        word = words[i] # заменяем значение 'word' на текущее, иначе 'if' ниже будет обрабатывать старое слово.
    if word[0] in signs:
        words[i] = word[1:]
    i+=1

for i in words:
    print(i, end=' ') 