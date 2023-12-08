# фибоначчи с использованием массива

def fib(n):
    F = list()
    F.append(0)
    F.append(1)

    for i in range(2, n):
        F.append(F[i - 1] + F[i - 2])

    return F[n - 1]


print(f" is {fib(int(input('fib numb of ')))}")
# fib numb of 10
#  is 34
