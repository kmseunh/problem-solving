n, m = map(int, input().split())

arr = [0] * (n + 1)

for _ in range(m):
    i, j, k = map(int, input().split())
    for o in range(i, j + 1):
        arr[o] = k

print(" ".join(map(str, arr[1:])))