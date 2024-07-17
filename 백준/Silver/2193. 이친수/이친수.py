import sys


def dp(x: int):
    d = [0] * (x + 1)
    d[1] = 1

    for i in range(2, x + 1):
        d[i] = d[i - 2] + d[i - 1]

    return d[x]


N = int(sys.stdin.readline())
print(dp(N))