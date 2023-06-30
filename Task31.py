# Задача №31.
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)
n = int(input('Введите число: '))

print(fib(n))

# def fibonchy(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibonchy(n-1) + fibonchy(n-2)


# print(fibonchy(7))
