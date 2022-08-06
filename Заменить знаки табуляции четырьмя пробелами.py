tab_file = open('tab.txt')
tab_text = tab_file.read() # все содержимое файла считывается в одну строку
tab_file.close()
print(repr(tab_text)) # функция repr используется, чтобы увидеть символы форматирования, такие как '\n', '\t', на самом деле метод read() тоже возвращает строку с этими символами, но в таком случае print() преобразовал бы эти символы в соот. действия

list_text = tab_text.split('\t')
space_text = '    '.join(list_text)
print(repr(space_text))

space_file = open('space.txt', 'w')
space_file.write(space_text)
space_file.close()