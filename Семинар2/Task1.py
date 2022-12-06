# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input('Введите вещественное число: '))
def summa(num):
    if float(num) < 0:
        x = float(num) * (-1)
    number = 0

    for i in str(num):
        if i != '.':
            number += int(i)
    return number


print(f'Сумма чисел равна {summa(num)}')
