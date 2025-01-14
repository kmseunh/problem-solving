n = int(input())

count = 1
end_room = 1

while n > end_room:
    end_room += count * 6
    count += 1

print(count)