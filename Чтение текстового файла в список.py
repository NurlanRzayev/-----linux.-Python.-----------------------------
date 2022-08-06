data = []
for i in open('data.txt'):
    data.append(i)
print(data)

for i in range(len(data)):
    if data[i][-1] == '\n':
        data[i] = data[i][:-1]
print(data)