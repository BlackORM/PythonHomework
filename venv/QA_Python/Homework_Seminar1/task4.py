# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

crane = int(input("Введите количество журавликов сделанных детьми: "))
if (crane%6 != 0):
    print ("Задача не имеет решения!")
else:
    print(f'Всего сделали {crane} журавликов. Из них Петя {int(crane/6)} Катя {int(crane/6*4)} Сережа {int(crane/6)}')