# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

num = int(input())
firstDigit = num % 10
num = num//10
secondDigit = num % 10
thirdDigit = num//10
print(firstDigit + secondDigit + thirdDigit)
