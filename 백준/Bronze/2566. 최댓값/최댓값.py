arr = [[0] * 9 for _ in range(9)]
max_num = 0
col = 0
row = 0

for i in range(9):
    values = list(map(int, input().split()))
    new_max_num = max(values)

    if new_max_num > max_num:
        max_num = new_max_num
        col = i
        row = values.index(new_max_num)

print(max_num)
print(col + 1, row + 1)