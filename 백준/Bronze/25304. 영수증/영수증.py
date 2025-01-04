x = int(input())
n = int(input())

money = 0

for _ in range(n):
    a, b = map(int, input().split())
    money += a * b

if money == x:
    print("Yes")
else:
    print("No")