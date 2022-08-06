from random import randint

def search(lst, item):
    mid = len(lst) // 2
    low = 0
    high = len(lst) - 1
    while lst[mid] != item and low <= high:
        if item > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2 # несмотря на то что len(lst) // 2 и (low + high) // 2, при low = 0, high = len(lst) - 1, не равны при нечетном high (четном len(lst)), бинарный поиск приведет к тому же значению если заменить mid = len(lst) // 2 в 4 строке программы на mid = (low + high) // 2, отсюда: произведя соответствующие изменения можно записать mid = (low + high) // 2 в начале цикла, см. "Двоичный поиск. Найти число в упорядоченном массиве.py"
    if low > high:
        return None
    else:
        return mid

a = []
for i in range(10):
    a.append(randint(1, 20))
a.sort()
print(a)

value = int(input())
print(search(a, value))
