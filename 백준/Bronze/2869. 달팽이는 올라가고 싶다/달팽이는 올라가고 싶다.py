import math

a, b, v = map(int, input().split())

if v <= a:
    print(1)
else:
    days = math.ceil((v - a) / (a - b)) + 1
    print(days)