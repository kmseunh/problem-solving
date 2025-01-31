while True:
    sides = list(map(int, input().split()))

    if sum(sides) == 0:
        break

    sides.sort()
    a, b, c = sides

    if c >= a + b:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")