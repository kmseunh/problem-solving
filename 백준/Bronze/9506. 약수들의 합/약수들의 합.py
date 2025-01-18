while True:
    n = int(input())

    if n == -1:
        break

    arr = []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            arr.append(i)
            if i != n // i and i != 1:
                arr.append(n // i)

    arr.sort()

    if sum(arr) == n:  # 완전수 판별
        print(f"{n} = {' + '.join(map(str, arr))}")
    else:
        print(f"{n} is NOT perfect.")