n1, n2, n3, n4, n5 = map(int, input().split())
sum = 0
arr = [n1, n2, n3, n4, n5]

for i in arr:
    sum += i**2

print(sum % 10)