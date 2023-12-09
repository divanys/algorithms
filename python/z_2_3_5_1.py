# По данным двум числам 1 ≤ a,b ≤ 2⋅10^9
# найдите их наибольший общий делитель.


# при помощи Евклидовой функции

def euvlid_gcd(a, b):
    if a == 0: return b
    elif b == 0: return a
    elif a >= b: return euvlid_gcd(a % b, b)
    elif b >= a: return euvlid_gcd(a, b % a)


def main():
    a, b = map(int, input().split())
    print(euvlid_gcd(a, b))


if __name__ == "__main__":
    main()

# 18 35
# 1

# 14159572 63967072
# 4