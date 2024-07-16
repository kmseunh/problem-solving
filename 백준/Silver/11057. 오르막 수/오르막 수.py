import sys


def dp(x: int):
    d = [[0] * 10 for _ in range(x + 1)]

    for i in range(10):
        d[1][i] = 1

    for i in range(2, x + 1):
        for j in range(10):
            d[i][j] = sum(d[i - 1][k] for k in range(j + 1))

    result = sum(d[x]) % 10007
    return result


N = int(sys.stdin.readline())

print(dp(N))