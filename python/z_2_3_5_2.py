# По данным двум числам 1 ≤ a,b ≤ 2⋅10^9
# найдите их наибольший общий делитель.


# наивна функция

def simple_stupid_fucking_angry_shit_fuck_fucking_fuck_simple_fun_GCD(a, b):
    gcd = 1
    for d in range(2, max(a, b) + 1):
        if a % d == 0 and b % d == 0:
            gcd = d

    return gcd

print(simple_stupid_fucking_angry_shit_fuck_fucking_fuck_simple_fun_GCD(int(input("a is ")), int(input("b is "))))

# НЕ ЗАПУСКАЙТЕ ЭТОТ ГЕНИАЛЬНЫЙ КОД ДЛЯ БОЛЬШИХ ЧИСЕЛ, Ю ДЕД ВИЛЛ ЭНД ЁР ПК ДЕД ВИЛЛ ТУ!!!!
# a is 18
# b is 51
# 3