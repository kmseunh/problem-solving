n, b = map(int, input().split())
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while n:
    result = digits[n % b] + result
    n //= b

print(result)