while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    arr = sorted([a, b, c])
    x, y, z = arr[0], arr[1], arr[2]

    if x**2 + y**2 == z**2:
        print("right")
    else:
        print("wrong")