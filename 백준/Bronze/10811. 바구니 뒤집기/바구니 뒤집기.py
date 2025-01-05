n, m = map(int, input().split())
arr = list(i for i in range(1, n + 1))

for _ in range(m):
    i, j = map(int, input().split())
    temp = arr[i - 1 : j]
    temp.reverse()
    arr[i - 1 : j] = temp

for n in arr:
    print(n, end=" ")