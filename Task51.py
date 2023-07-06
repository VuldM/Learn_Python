# Задача №51.
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: 
values = [0, 2, 4, 10, 6]

# def same_by(characteristic, objects):
#      list_0 = list(map(characteristic, objects))
#      if list_0.count(1) == 1:
#          return False
#      else:
#          return True

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
# Вывод:
# same
def same_by(characteristic, objects):
    return len(objects) == len(list(filter(characteristic, objects)))

print(same_by(lambda x: x % 2 != 0, values))

if same_by(lambda x: x%2 == 0 , values):
    print('same')
else:
    print('different')