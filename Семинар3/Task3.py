#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform
N = int(input('Введите размер списка: '))
list = []
for i in range(N):
    a = uniform(0, 9)
    list.append(round(a, 2))

min = list[0]
max = 0
for i in range(len(list)):

    if max < list[i]:
        max = list[i]
    if min > list[i]:
        min = list[i]
diff = (max - int(max)) - (min - int(min))

print(list)
print(max, min)
print(round(diff, 2))
