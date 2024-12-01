S = input()

alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
    "u", "v", "w", "x", "y", "z"
]

arr = [-1] * 26

for idx, char in enumerate(S):
    if arr[alphabet.index(char)] == -1:
        arr[alphabet.index(char)] = idx

print(" ".join(map(str, arr)))