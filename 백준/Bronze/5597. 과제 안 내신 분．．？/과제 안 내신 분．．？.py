arr = []
check_arr = []

for _ in range(28):
    n = int(input())
    arr.append(n)

for i in range(1, 31):
    if i not in arr:
        check_arr.append(i)

check_arr.sort()

for num in check_arr:
    print(num, end="\n")