a = int(input())
b = int(input())

units = (b % 10) * a
tens = ((b // 10) % 10) * a
hundreds = (b // 100) * a

print(units)
print(tens)
print(hundreds)
print(a * b)