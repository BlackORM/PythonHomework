# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел A i. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
n = int(input('Введите количество элементов массива: '))
a = []
for i in range(n):
    a.append(int(input(f'Введите A[{i + 1}] элемент: ')))
num = int(input('Введите число: '))
count = 0
for i in range(n):
    if a[i] == num:
        count += 1
print(f'Число {num} в массиве {a} встречается {count} раз(а)!')
