# Задача 12:
# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
s = int(input('Введите сумму загаданых чисел: '))
p = int(input('Введите произведение загаданых чисел: '))
k = 0
i = 1
v = 0
while i <= p:
    k = p / i
    if p%i == 0:
        if k + i == s:
            v = 1
            print(f'загаданные числа {int (k)} и {int (i)}')
            break
    i = i + 1  
if v == 0: print('Задуманные числа не могут быть суммой и произведением загаданных чисел.')