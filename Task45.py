# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:                   Вывод:
# 300                     220 284
list_0 = []
m = 0
for i in range(2, n):
    for j in range(1, i):
        if i%j == 0: 
            m = m + int(i/j)
            print(f'{i}/{j} = {int(i/j)}')
    list_0.append(m)     
    print(f'Сумма делителей числа {i} равна {m}')
    m = 0    
for i in list_0:
    if list_0.count(i) > 1:
        print(list_0.index(i))
print(list_0)

def summ(k):
    summa=0
    for i in range(1,k//2+1):
        if k%i==0:
            summa+=i
    return summa

n=int(input("Введите число n: "))
for i in range(n):
    for j in range(i):
        if summ(i)==j and summ(j)==i and i!=j:
            print(f'{i} {j}')
            def summ_del(num):
    sum1 = 0
    for i in range(1, num):
       if num % i == 0:
           sum1 += i
    return sum1

third = []
for i in range(1, 20000):
    second = summ_del(i)
    first = summ_del(second)
    if i == first and i < second:
        print(i, second)