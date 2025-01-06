dial = [
    "ABC",
    "DEF",
    "GHI",
    "JKL",
    "MNO",
    "PQRS",
    "TUV",
    "WXYZ",
]

time = 0

word = input()

for i in dial:
    for j in word:
        if j in i:
            time += dial.index(i) + 2

print(time + len(word))