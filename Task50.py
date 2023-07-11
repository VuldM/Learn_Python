# Задача №49.
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def add_contact():
    index = 0
    flag = True
    while flag:
         ex_out = input('Добавить да/нет нажимте y or n: ')               
         if ex_out == 'y':
            file_contact = open('contact.txt', 'a', encoding='UTF-8')
            add_FIO = input('Введите фамилию, имя, отчество: ')
            add_phone_num = input('Введите номер телефона: ')
            if add_phone_num.isdigit():
                  file_contact.write(add_FIO +' '+ add_phone_num + '\n')
                  file_contact.close
                  flag = False
                  add_contact()
            else:
                print('Вы ввели не цифры')
                file_contact.close
                continue                        
         elif ex_out =='n':                          
             flag = False             
         else:
             print('Такой команды нет')
             continue
def search_contact(): 
    name_user = open('contact.txt', 'r', encoding='UTF-8')
    flag = True    
    ex_out = input('Найти контакт да/нет нажимте y or n: ') 
    if ex_out == 'y':
            search_name = input('Введите имя или фамилию: ')
            while flag:                
                all_file = name_user.readline()                     
                if search_name in all_file:
                    print(all_file)                      
                elif not all_file:
                    print('Достигнут конец списка')
                    flag = False
                    name_user.close()     
    elif ex_out == 'n':
             choice_user()   
    else:
        print('Такой команды нет')
        
def del_contact():  
    name_user = open('contact.txt', 'r', encoding='UTF-8')          
    ex_out = input('Удалить контакт да/нет нажимте y or n: ') 
    if ex_out == 'y':
        search_name = input('Введите имя или фамилию: ')
        flag = True
        while flag:                
            all_file = name_user.readline()                     
            if search_name in all_file:
                print(all_file)                      
            elif not all_file:
                print('Достигнут конец списка')
                flag = False
                name_user.close() 
        del_pos = int(input('С какой позиции удалить контакт? '))   
        del_pos = del_pos - 1         
        name_us_del = open('contact.txt', 'r', encoding='UTF-8')          
        list_name = name_us_del.readlines()                      
        print(list_name)
        if (del_pos >= 0) and (del_pos < len(list_name)):      
             index = del_pos
             while index <  len(list_name) - 1:
                list_name[index] = list_name[index + 1]
                index = index + 1
             list_name = list_name[:-1]                        
        name_us_del.close()                                 
        name_us_del = open('contact.txt', 'w', encoding='UTF-8')        
        for line in list_name:                        
           name_us_del.write(line)
        name_us_del.close()                                
    elif ex_out == 'n':
        choice_user()   
    else:
        print('Такой команды нет')
    

def choice_user():
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
                # del_contact()
                flag = False
             case _:
                print('такой команды нет.')
                flag = False
choice_user()
