# Задача 22:
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
n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
print(n, m)
list_1 = []
list_2 = []
for _ in range(n):
   # plenty_1.add(int(input('Вводите элементы в первое множество:')))
   list_1.append(random.randint(1, 30))
for _ in range(m):
    #plenty_2.add(int(input('Вводите элементы во второе множество:'))) 
    list_2.append(random.randint(1, 30))
plenty_1 = set(list_1)
plenty_2 = set(list_2)
inter_sect = plenty_1.intersection(plenty_2)
print(list_1)
print(list_2)
print(sorted(inter_sect))
