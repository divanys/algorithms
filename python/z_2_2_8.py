# Даны целые числа 1 ≤ n ≤ 10^18 и 2 ≤ m ≤ 10^5,
# необходимо найти остаток от деления n-го числа Фибоначчи на m.

# числа фибоначчи искать здесь - это самоубийство
# F(n) mod m = ((F(n-2) mod m) + (F(n-1) mod m) ) mod m - формула пизано примерно


def find_fibonacci_modulo(n, m):
    pisano_period = [0, 1]
    i = 2
    while True:
        pisano_period.append((pisano_period[i - 1] + pisano_period[i - 2]) % m)
        if pisano_period[i] == 1 and pisano_period[i - 1] == 0:
            break
        i += 1

    pisano_length = len(pisano_period) - 2
    remainder = n % pisano_length

    return pisano_period[remainder]


n, m = map(int, input("Введит n m: ").split())

result = find_fibonacci_modulo(n, m)
print(result)

# Введит n m: 10 2
# 1
