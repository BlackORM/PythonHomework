# 3.Создайте список из случайных чисел.
# Найдите максимальное количество его одинаковых элементов.

import random
n = int(input('Введите длину списка: '))
a = []
max = 0
for i in range(n):
    a.append(random.randint(1, 10))
print(a)

count = {}

for num in a:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
    if count[num] > max:
        max = count[num]
print(f'Словарь элементов: {count}')
print (f'Максимальное количество одинаковых элементов: {max}')
