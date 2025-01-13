t = int(input())

for _ in range(t):
    c = int(input())
    coins = [25, 10, 5, 1]
    result = []

    for coin in coins:
        result.append(c // coin)
        c %= coin

    print(*result)