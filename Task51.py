# Напишите функцию same_by(characteristic, objects), 
# которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
# и возвращают True, если это так. 
# Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, 
# которая принимает объект и вычисляет его характеристику.
# Ввод:							Вывод:
# values = [0, 2, 10, 6]				same
# if same_by(lambda x: x % 2, values):
# 	print(‘same’)
# else:
# 	print(‘different’)

def same_by(characteristic, objects):
    result = list(filter(characteristic, objects))
    return len(result) == len(objects)


values = [0, 2, 10, 6]

if same_by(lambda x: True if x%2 == 0 else False, values):
    print('same')
else:
    print('different')

# def same_by(characteristic,values):
#     return len(list(filter(characteristic,values)))==len(values)
#
# values = [3, 5, 1]
# if same_by(lambda x: True if x % 2 == 1 else False, values):
#     print('same')
# else:
#     print('different')    