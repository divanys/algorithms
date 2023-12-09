# По данным двум числам 1 ≤ a,b ≤ 2⋅10^9
# найдите их наибольший общий делитель.


a, b = map(int, input().split())
while b:     # while b != 0
    a, b = b, a % b
print(a)