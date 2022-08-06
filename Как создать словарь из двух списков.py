a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']

c = {}
for i in range(len(a)):
    c[a[i]] = b[i]
# or c = dict(zip(a, b))
print(c)