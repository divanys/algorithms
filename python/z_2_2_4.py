# фибоначчи с использованием массива (занимает очень много операций, т.к. экспоненциальный рост из-за дерева рекурсии)

def fib(n):
    if n <= 1: return n
    else: return fib(n - 1) + fib(n - 2)

print(f" is {fib(int(input('fib numb of ')))}")
# fib numb of 9
#  is 34
