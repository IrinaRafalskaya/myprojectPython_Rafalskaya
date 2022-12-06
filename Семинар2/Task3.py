# Задайте список из n чисел последовательности (1+1/N)^N выведите на экран их сумму

n = int(input('Введите количество чисел: '))

def numbers(n):
    sum = 0
    for i in range(n):
        a = int(input(f'Введите число {i + 1} :'))
        a = (1+1/a)**a
        sum = a + sum
        i += 1
    return sum

print('Сумма чисел равна',round((numbers(n)), 2))