a, b, c = list(map(int, input().split()))
money = 0

if a == b == c:
    money = 10000 + a * 1000
elif a == b:
    money = 1000 + a * 100
elif b == c:
    money = 1000 + b * 100
elif c == a:
    money = 1000 + c * 100
else:
    money = max(a, b, c) * 100

print(money)