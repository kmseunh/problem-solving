import sys


def dp(x: int):
    d = [[0] * 10 for _ in range(x + 1)]

    for i in range(10):
        if i == 0:
            d[1][i] = 0
        else:
            d[1][i] = 1

    for i in range(2, x + 1):
        for j in range(10):
            if j == 0:
                d[i][j] = d[i - 1][j + 1]
            elif j == 9:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = d[i - 1][j + 1] + d[i - 1][j - 1]

    result = sum(d[x]) % 1000000000
    return result


N = int(sys.stdin.readline())

print(dp(N))