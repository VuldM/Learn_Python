# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
a = int(input('Введите число: '))
n = int(input('Введите степень числа: '))
def power_rec(a, n):
    if n == 0: return 1
    else: return power_rec(a, n - 1) * a
print(f'Ваш результат: {a}^{n} = {power_rec(a, n)}')