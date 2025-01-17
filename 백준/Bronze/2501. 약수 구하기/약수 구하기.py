n, k = map(int, input().split())
arr = set()

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        arr.add(i)
        arr.add(n // i)

sorted_arr = sorted(arr)

if k <= len(sorted_arr):
    print(sorted_arr[k - 1])
else:
    print(0)