# Задача №39.
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:                        Вывод:
# 7                           3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1       (каждое число вводится с новой строки)
n = int(input('Введите количество элементов певрого массива: '))
list_1 = []
for i in range(n):
    list_1.append(int(input('Введите значение:')))
  
m = int(input('Введите количество элементов второго массива: '))
list_2 = []
for i in range(m):
    list_2.append(int(input('Введите значение:')))
list_1 = [3, 1, 3, 4, 2, 4, 12]
list_2 = [4, 15, 43, 1, 15, 1 ]
list_3 = []
print(list_1)      
print(list_2)
for i in range(len(list_1)):
        if list_1[i] not in list_2:  
            list_3.append(list_1[i])           
print(list_3) 

import random

print(first := [random.randint(0, 10) for _ in range(int(input('Размер первого списка: ')))])
print(second := [random.randint(0, 10) for _ in range(int(input('Размер второго списка: ')))])

print([item for item in first if item not in second])