word = list(input().upper())
cnt = []

for char in set(word):
    count = word.count(char)
    cnt.append((char, count))

max_count = max(cnt, key=lambda x: x[1])[1]

mode = [char for char, count in cnt if count == max_count]

print("?" if len(mode) > 1 else mode[0])