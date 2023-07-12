dict_0 = {'Михайлиди Владимир Михайлович': 89042706753, 'Михайлиди Ирина Николаевна': 89042704917, 'Михайлиди Артем Владимирович': 89087149143,
           'Михайлиди Арина Владимировна': 89087188816, 'Кунц Сергей Николаевич':8908456123}

print(list(dict_0.keys()))
name = input('Введите имя')
for i in list(dict_0.keys()):
    if name.lower() in i.lower():
        print(f'{i} {dict_0.get(i)}')
        dict_0.pop(i)
print(dict_0)
name = input('Введите имя')
vall = int(input('Введите новый номер телефона: '))
for i in list(dict_0.keys()):
    if name.lower() in i.lower():
        print(f'{i} {dict_0.get(i)}')
        dict_0[i] = vall
print(dict_0)