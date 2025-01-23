x_arr = []
y_arr = []

for _ in range(3):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)

x4 = 0
y4 = 0

for x in x_arr:
    x4 ^= x
for y in y_arr:
    y4 ^= y

print(x4, y4)