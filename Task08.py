#Задача 8:
#Требуется определить, можно ли от шоколадки размером n × m долек
#отломить k долек, если разрешается сделать один разлом по прямой между дольками
#(то есть разломить шоколадку на два прямоугольника).
#*Пример:*
#3 2 4 -> yes
#3 2 1 -> no
n = int(input('Сколько долек по длине шоколадки?: '))
m = int(input('Сколько долек по ширине шоколадки?: '))
k = int(input('Сколько долек хотели бы отломить?: '))
if k % n == 0 or k % m == 0 and k < n * m:
    print('Да, у вас получится это сделать.')
else:
    print('Нет, это не возможно')