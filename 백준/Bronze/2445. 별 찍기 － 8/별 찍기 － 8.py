N = int(input())

for i in range(1, 2 * N):
    if i <= N:
        stars = i
    else:
        stars = 2 * N - i

    spaces = 2 * (N - stars)
    print("*" * stars + " " * spaces + "*" * stars)