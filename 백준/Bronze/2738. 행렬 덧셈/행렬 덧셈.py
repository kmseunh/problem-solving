n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

for _ in range(2):
    for i in range(n):
        values = list(map(int, input().split()))
        for j in range(m):
            arr[i][j] += values[j]

for row in arr:
    print(" ".join(map(str, row)))