
dict_0 = {'Михайлиди Владимир Михайлович': 89042706753,  'Михайлиди Ирина Николаевна': 89042704917, 'Михайлиди Артем Владимирович': 89087149043, 'Михайлиди Арина Владимировнм': 89087188816}
print(dict_0)
w = open('dict.txt', 'w', encoding='UTF-8')
for key, value in dict_0.items(): #записываем словать в файл
    w.write('%s: %s\n' % (key, value))
w.close()

with open('contact.txt', 'r', encoding='UTF-8') as file: #Читаем файл
    lines = file.read().splitlines() # read().splitlines() - чтобы небыло пустых строк
dic = {} # Создаем пустой словарь
for line in lines: # Проходимся по каждой строчке
  key,value = line.split(': ') # Разделяем каждую строку по двоеточии
  dic.update({key:value})	 # Добавляем в словарь
  if not lines:
     print('конец списка')
print(dic) # Вывод словаря на консоль
dict_0 = dic['4 Михайлиди Ирина Николаевна']
print(dict_0)

dic_key = input('Введите ключ ')
dic_vol = input('Введите значение ')
dic[dic_key] = dic_vol     # добавляет ключ - значения в словарь. также и его можно изментиь введя действующий ключ и другое значение
print(dic)
del dic[input('ввведите что удалить')]
print(dic)