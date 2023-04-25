# Даны два массива чисел. 
# Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), 
# которых нет во втором массиве. 
# Пользователь вводит  число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива
# Ввод: 					Вывод:
# 7					3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1			(каждое число вводится с новой строки)

# N = int(input("Введите колво элементов 1го массива"))
# a = []
# for i in range(N):
#     a.append(input())
# M = int(input("Введите колво элементов 2го массива"))
# b = []
# for i in range(M):
#     b.append(input())
# c = []
# for i in a:
#     flag = False
#     for j in b:
#         if i == j:
#             flag = True
#             break
#     if flag == False:
#         c.append(i)
# print(c)

n = int(input())
lst_1 = []
for i in range(n):
    lst_1.append(int(input()))
m = int(input())
lst_2 = []
for i in range(m):
    lst_2.append(int(input()))
for i in lst_1:
    if i not in lst_2:
        print(i, end = " ")
        

