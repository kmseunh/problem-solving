max_num = 0
row, col = 0, 0

for i in range(9):
    values = list(map(int, input().split()))
    new_max_num = max(values)
    
    if new_max_num > max_num:
        max_num = new_max_num
        row, col = i, values.index(new_max_num)

print(max_num)
print(row + 1, col + 1)