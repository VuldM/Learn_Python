# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# text = '1234567895466666'
# temp = {}

# for i in range(len(text)):
#     temp[text[i]] = 0
# # print(temp)

# for i in range(len(text)):
#     if text[i] in temp.keys():
#         temp[text[i]] += 1
# print(temp)
text = 'aaabcaadcdd'
dict_count = {}
for n in text:
    dict_count[n] = dict_count.get(n, 0 ) + 1
    if dict_count.get(n) < 2:
        print(n, end = ' ')
    else:
        print(f'{n}_{dict_count.get(n) - 1}', end = ' ')   