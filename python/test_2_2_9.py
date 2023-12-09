# фибоначчи с использованием массива (занимает ~ 2n операций)
# нужно доказать (доказала в тетрадке):  ∑([n, i = 0], F[i]) = F[n + 2] − 1.
# здесь просто проверяю)


def fib(n):
    F = list()
    F.append(0)
    F.append(1)

    for i in range(2, n + 1):
        F.append(F[i - 1] + F[i - 2])

    b, a = F[-1], F[-2]
    b, a = a + b, b
    b, a = a + b, b  # увеличиваем до n + 2 (глупо, но рабоче))

    return [F[n], sum(F), b - 1]


intF = int(input('fib numb of '))
res = fib(intF)
print(f" is {res[0]}")
print(f" sum is {res[1]}")
print(f" test is {res[-1]}")
# fib numb of 5
#  is 5
#  sum is 12
#  test is 12