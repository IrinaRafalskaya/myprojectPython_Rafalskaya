# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите натуральное число: "))
i = 2
list = []
multipliers = num
while i <= num:
    if num % i == 0:
        list.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {multipliers} являются: {list}")
