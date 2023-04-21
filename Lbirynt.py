# Напишите программу, которая находит путь в лабиринте между заданными клетками. Сведения о лабиринте (размеры, расположение стенок, координаты начальной и целевой клеток) записаны в файле input.txt . Требуется найти и вывести длину кратчайшего маршрута между заданными начальной и целевой клетками.

# Входные данные
# В первой строке файла input.txt записаны через пробел размеры карты лабиринта: количество строк N и количество столбцов M ( 1 ≤ N , M ≤ 100 ).

# Далее в отдельной строке через пробел записаны координаты начальной клетки, сначала строка, потом столбец (нумерация с единицы!). В следующей строке в таком же формате записаны координаты целевой клетки, в которую нужно придти.

# В следующих N строках записана карта лабиринта. 
# Каждая строка состоит из M символов, каждый символ – это '.' (клетка свободна)
#  или 'X' (клетка непроходима).
# Выходные данные
# Программа должна вывести одно число – 
# длину кратчайшего маршрута из начальной клетки лабиринта в целевую. 
# Если таких маршрутов нет, нужно вывести число -1.
# Примеры
# входные данные
# 6 7
# 1 2
# 2 6
# ....X..
# .XXXX..
# ....X..
# ....X..
# XX.XX.X
# ......X
# выходные данные
# 15
