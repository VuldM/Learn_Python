# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
n = int(input('Введите конечную степень числа 2: '))
m = 0
for i in range(0, n, 2):
    print(f'{2**i}')
    