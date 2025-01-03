a, b = map(int, input().split())
c = int(input())

hours = (a + ((b + c) // 60)) % 24
minutes = (b + c) % 60

print(hours, minutes)
