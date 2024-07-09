N = int(input())

for i in range(1, 2 * N):
    if i <= N:
        stars = "*" * (2 * N - (2 * i - 1))
        spaces = " " * (i - 1)
    else:
        stars = "*" * (2 * (i - N) + 1)
        spaces = " " * (2 * N - i - 1)

    print(spaces + stars)