n = int(input())
x_arr = []
y_arr = []

if n == 1:
    print(0)
else:
    for _ in range(n):
        x, y = map(int, input().split())
        x_arr.append(x)
        y_arr.append(y)

    line1 = max(x_arr) - min(x_arr)
    line2 = max(y_arr) - min(y_arr)

    print(line1 * line2)