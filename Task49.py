# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# # print(*find_farthest_orbit(orbits))
# # Вывод:
# # 2.5 10
# import math
# orbits = [(1, 3), (2.5, 10), (7, 7), (6, 6), (4, 3)]
# def find_farthest_orbit(orbit):    
#     list_s = [[orbit[i][j] for j in range(2)] for i in range(len(orbit))if orbit[i][0] != orbit[i][1]]
#     min_s = 0.0
#     max_s = []       
#     for i in range(len(list_s)):
#             if round(math.pi*(list_s[i][0] * list_s[i][1]), 2) > min_s:
#                  max_s= (list_s[i][0],list_s[i][1]) #.append([list_s[i][0],list_s[i][1]]) 
#                  min_s = round(math.pi*(list_s[i][0] * list_s[i][1]), 2)
                
#     return max_s

# print(find_farthest_orbit(orbits))

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(data := list(filter(lambda x: not x[0] == x[1], orbits)))
# print(res := list(map(lambda x: x[0]*x[1]*3.14, data)))
# print(orbits[res.index(max(res))])

MTN_SIZE = 1
MAX_SIZE = 10
PNANETS = 12
import random
def planets(min_size: int, max_size: int, planet: int) -> list[tuple[int, int]]:
      def ellipse(minn: int, maxx: int, count: int):
            return [random.randint(minn, maxx) for _ in range(count)]
      return list(zip(ellipse(min_size, max_size, planet), ellipse(min_size, max_size, planet)))

print(all_planets := planets(MTN_SIZE, MAX_SIZE, PNANETS))
print(all_planets := list(filter(lambda x: x[0] != x[1], all_planets)))
print(max(all_planets, key=lambda x: x[0] * x[1]))

      