# 4.Создайте список из случайных чисел. Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2

import random
n = int(input('Введите длину списка: '))
a = []
max1 = max2 = 0
for i in range(n):
    a.append(random.randint(1, 10))
    if a[i] > max1:
        max1 = a[i]
print(a)
for i in range(n):
    if a[i] > max2 and a[i] != max1:
        max2 = a[i]
print (f'Первый максимум {max1}, второй максимум {max2}')

