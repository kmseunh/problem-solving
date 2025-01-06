dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

word = input()
time = 0

for char in word:
    for idx, group in enumerate(dial):
        if char in group:
            time += idx + 3

print(time)