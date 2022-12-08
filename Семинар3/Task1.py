# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint
list = [randint(-10, 10) for i in range(10)]
summ = 0
for i in range(1, len(list), 2):
    if i % 2 == 1:
        summ += list[i]
print(f"{list} -> сумма элементов на нечётных позициях: {summ}")