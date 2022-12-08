#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

N = int(input('Введите число: '))

def fibonacci(N):
    fibo_num = []
    a, b = 1, 1
    for i in range(N-1):
        fibo_num.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (N):
        fibo_num.insert(0, a)
        a, b = b, a - b
    return fibo_num

fibo_num = fibonacci(N)
print(fibonacci(N))
print(fibo_num.index(0))