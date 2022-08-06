def list_avrg(lst):
    l = len(lst)
    sum = 0
    for i in lst:
        sum += i
    return sum / l

print('Input integers:')
a = input()
a = a.split()
for i in range(len(a)):
    a[i] = int(a[i])

avrg = list_avrg(a)

print('Average:')
print(round(avrg, 2))
