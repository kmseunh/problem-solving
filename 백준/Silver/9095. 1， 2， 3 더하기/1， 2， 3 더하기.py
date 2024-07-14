import sys

n = int(input())


def dp(x: int):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return dp(x - 1) + dp(x - 2) + dp(x - 3)


for _ in range(n):
    t = int(sys.stdin.readline())
    print(dp(t))