chess = [1, 1, 2, 2, 2, 8]

item = list(map(int, input().split()))

for i in range(6):
    print(chess[i] - item[i], end=" ")