# Задача №47.
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# Ввод:
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print('ok')
# else:
#  print('fail')
# Вывод:   ok
values = [1, 23, 42, 'asdfg', 2, 3, 5 , 7 , 25 , 36 , ]
def trasformation(a):
    return a
transformed_values = list(map(trasformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
def func(a):
    #####################################################
    return a + a
x = map(func, [1, 2, 4, 6]) # x - это объект типа map по очередно обращается к значениям в списке и производит над ними операции функции
print(x)
print(set(x))

list_0 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
newtuple = map(lambda n: n+4 , list_0) # тоже самое что и выше, только в одной сроке
print(list(newtuple)) 

def func(x):
    if x>=3:
        return x
y = filter(func, (1,2,3,4))  #по очередно обращается к значениям в списке и проверяет условие заданое в функции
print(y)
print(list(y))

y = filter(lambda x: (x>=3), (1,2,3,4)) # тоже самое что и выше, только в одну сроку
print(list(y))

from functools import reduce #    10 + 2 + 3 + 4
print(reduce(lambda a, b: a + b, [10,  2,  3,  4])) #складывает по парно значения в списке в соответствии с очередностью заданную переменными а, b
from functools import reduce #    10 - 2 - 3 - 4
print(reduce(lambda a, b: a - b, [10,  2,  3,  4]))
from functools import reduce #    2 + 10 + 4 + 3
print(reduce(lambda a, b: b + a, [10,  2,  3,  4]))
from functools import reduce #    2 - 10 + 4 - 3
print(reduce(lambda a, b: b - a, [10,  2,  3,  4]))

c = map(lambda x:x+x,filter(lambda x: (x>=3), (1,2,3,4)))#сначала выполняется сравнение, затем вычесление
print(list(c))

c = filter(lambda x: (x>=3),map(lambda x:x+x, (1,2,3,4)))#сначала выполняются вычисления, затем сложение
print(list(c))

d = reduce(lambda x,y: x+y,map(lambda x:x+x,filter(lambda x: (x>=3), (1,2,3,4)))) 
print(d)
# cначала проверяет условие в кортеже(списке) filter(3, 4), затем складывает результат сами с собой map(3+3=6, 4+4=8),
# затем складывает результа друг с другом reduce(6 + 8)  в примере выше.                                                               
