# Задача №21.
# Напишите программу для печати всех уникальных
# значений в словаре.

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит
list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
list_2 = set()
for item in list_1:
    for i in item.values():
        list_2.add(i)
print(list_2) 

print(set(v for i in range(len(list_1)) for (k, v) in list_1[i].items()))

print({[value for value in item.values()] [0] for item in list_1})