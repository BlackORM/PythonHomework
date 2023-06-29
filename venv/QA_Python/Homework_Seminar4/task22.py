# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random
n = int(input('Введите количество элементов первой последовательности: '))
first = []
for _ in range(n):
    first.append(random.randint(1, 10))
m = int(input('Введите количество элементов второй последовательности: '))
second = []
for _ in range(m):
    second.append(random.randint(1, 10))
print(*first)
print(*second)
first = set(first)
second = set(second)
result = first.intersection(second)
if len(result) == 0:
    print('Нет общих значений!')
else:
    print(*sorted(result))

