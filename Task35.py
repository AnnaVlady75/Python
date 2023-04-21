# Напишите функцию, которая принимает одно число
# и проверяет, является ли оно простым
# Напоминание: Простое число - это число, 
# которое имеет 2 делителя: 1  и n(само число)
# Input: 5
# Output: yes

# def is_prime(num, i = 2):
#     if num <= 1:
#         return 'input more than 1'
#     elif i >= num/2:
#         return 'number is prime'
#     elif num % i == 0:
#         return 'number is not prime'
#     return is_prime(num, i + 1)
# print(is_prime(5))

def simple(n):
    for i in range(2, int(pow(n, 0.5))):
        if n%i == 0:
            return False
    return True
print(simple(117))


    

