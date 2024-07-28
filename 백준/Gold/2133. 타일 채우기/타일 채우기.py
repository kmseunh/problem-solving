import sys


def solve(n):
    if n % 2 != 0:
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3

    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3
        for j in range(0, i - 4 + 1, 2):
            dp[i] += dp[j] * 2

    return dp[n]


input = sys.stdin.readline

n = int(input())
print(solve(n))