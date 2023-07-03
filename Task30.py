# Задача 30:
# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии:
# An = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
list_0 = []
first_element = int(input('Введите первый элемент: '))
difference = int(input('Введите разность: '))
numbers = int(input('Введите количество элементов в массиве: '))

for i in range(1, numbers + 1):
    ar_progress = first_element + (i - 1) * difference
#    print(ar_progress, end=' ' )
    list_0.append(ar_progress)
print(list_0)