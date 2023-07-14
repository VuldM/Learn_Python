# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.
tel_user = {}

def add_contact():
    flag = True
    while flag:
         ex_out = input('Добавить да/нет нажимте y or n: ')               
         if ex_out == 'y':
            name = input('Введите ФИО и номер телефона: ')
            tel = input('Введите номер телефона: ')
            tel_user.setdefault(name, tel)  # если свободен ключ записывает ключ - значение
            print(tel_user)                              
         elif ex_out =='n':                          
             flag = False 
             choice_user()                     
         else:
             print('Такой команды нет')
             continue
def search_contact():
    flag = True 
    while flag:
        ex_out = input('Найти контакт да/нет нажимте y or n: ') 
        if ex_out == 'y':
         search_name = input('Введите имя или фамилию: ')               
         for i in list(tel_user.keys()):
            if search_name.lower() in i.lower():
               print(f'{i} {tel_user.get(i)}')   
        elif ex_out == 'n':
              flag = False
              choice_user()  
        else:
              print('Такой команды нет')
def del_contact():
    flag = True 
    while flag:
        ex_out = input('Удалить контакт да/нет нажимте y or n: ') 
        if ex_out == 'y':
         search_name = input('Введите имя или фамилию контакта который хотите удалить: ')               
         for i in list(tel_user.keys()):
            if search_name.lower() in i.lower():
               print(f'{i} {tel_user.get(i)}')  
               tel_user.pop(i)
         print(tel_user) 
        elif ex_out == 'n':
              flag = False
              choice_user()  
        else:
              print('Такой команды нет')
def choice_user():
    file = open('tel_contact.txt', 'r', encoding='utf-8')
    lines = file.read().splitlines()
    file.close
    for line in lines: # Проходимся по каждой строчке
       key,value = line.split(': ') # Разделяем каждую строку по двоеточии
       tel_user.update({key:value})	 # Добавляем в словарь
    print(tel_user)
    flag = True
    choice = input('добавить контакт нажимте "a", найти контакт нажмите "s", удалить контакт нажмита "d"')
    while  flag:        
        match choice:
             case 'a':
                add_contact() 
                flag = False
             case 's':
                search_contact()
                flag = False
             case 'd':
                del_contact()
                flag = False
             case _:
                print('такой команды нет.')
                flag = False
    file = open('tel_contact.txt', 'w', encoding='utf-8')
    for key, value in tel_user.items(): #записываем словаpь в файл
        file.write('%s: %s\n' % (key, value))
    file.close()

choice_user()