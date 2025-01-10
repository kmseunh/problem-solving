arr = []

for _ in range(5):
    arr.append(input())

result = ""
max_length = max(len(row) for row in arr)

for i in range(max_length):
    for row in arr:
        if i < len(row):
            result += row[i]

print(result)