T = int(input())

for _ in range(T):
    string = ""

    R, S = input().split()
    R = int(R)

    for word in S:
        string += word * R

    print(string)
