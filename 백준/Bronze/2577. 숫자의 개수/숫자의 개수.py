A = int(input())
B = int(input())
C = int(input())

mult = A * B * C
arr = list(map(int, str(mult)))
result = [0] * 10

for num in arr:
    result[num] += 1

for count in result:
    print(count)