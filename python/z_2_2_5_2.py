# фибоначчи с использованием 2 переменных

def fib(n):
    a, b = 0, 1
    for i in range(2, n):  # с учётом, что нулевой - это первый при вводе n
        a, b = b, a + b

    return b


print(f" is {fib(int(input('fib numb of ')))}")
# fib numb of 10
#  is 34
