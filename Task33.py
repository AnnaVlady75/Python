# Хакер Василий получил доступ к классному журналу 
# и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# def max_min(marks):
#     max_number = max(marks)
#     min_number = min(marks)
#     for i in range(len(marks)):
#         if marks[i] == max_number:
#             marks[i] = min_number
#     return marks

# a = [1, 3, 4, 5, 5, 2]
# print(max_min(a))    

a = input().split()
for i in range(len(a)):
    i = int(a[i])
max_el = max(a)
min_el = min(a)
for i in range(len(a)):
    if a[i] == max_el:
        a[i] == min_el
print(a)            