import math

n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

tot_shirt = 0
for size in sizes:
    if size > 0:
        tot_shirt += math.ceil(size / t)

single_pen = n % p
tot_pen = n // p

print(tot_shirt)
print(tot_pen, single_pen)