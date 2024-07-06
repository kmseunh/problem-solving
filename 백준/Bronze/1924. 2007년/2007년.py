month, day = map(int, input().split())

thirty = [4, 6, 9, 11]
thirty1 = [1, 3, 5, 7, 8, 10]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

for i in range(1, month):
    if i in thirty:
        day += 30
    elif i in thirty1:
        day += 31
    else:
        day += 28


print(week[day % 7])