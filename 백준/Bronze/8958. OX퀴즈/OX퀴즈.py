T = int(input())

for _ in range(T):
    score = 0
    count = 0
    result = input()
    for char in result:
        if char == "O":
            count += 1
            score += count
        else:
            count = 0
    print(score)