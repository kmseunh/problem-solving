scale = [1, 2, 3, 4, 5, 6, 7, 8]
reversed_scale = scale[::-1]

arr = list(map(int, input().split()))

if arr == scale:
    print("ascending")
elif arr == reversed_scale:
    print("descending")
else:
    print("mixed")