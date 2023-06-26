# Задача №19.
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
import random
print(my_list := [random.randint(0, 5) for _ in range(10)])
shift = int(input('Введите сдвиг: '))

for i in range(len(my_list)):
    print(my_list[(i-shift)%len(my_list)], end=' ')

print('\n' + str(my_list[-shift:] + my_list[:-shift]))

for _ in range(shift):
    my_list.insert(0, my_list.pop())
print(my_list)