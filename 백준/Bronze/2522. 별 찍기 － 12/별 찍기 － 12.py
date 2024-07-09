N = int(input())

for i in range(1, 2 * N):
    if i <= N:
        stars = "*" * i
        spaces = " " * (N - i)
    else:
        stars = "*" * (2 * N - i)
        spaces = " " * (i - N)

    print(spaces + stars)