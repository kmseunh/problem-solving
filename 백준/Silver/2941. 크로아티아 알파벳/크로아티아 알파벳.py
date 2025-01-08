alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word: str = input()

for i in alphabet:
    word = word.replace(i, " ")
    
print(len(word))