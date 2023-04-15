# Напишите программу для печати всех уникальных значений в словаре.
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит


list = [{"V": "S001", "V": "S002", "VI": "S001", "VI": "S005",
         "VII": " S005 ", " V ": " S009 ", " VIII ": " S007 "}]
# print(type(list))
set_uniq = set()
for dct in list:
    for key, value in dct.values():
        set_uniq.add(value.strip())
print(set_uniq)