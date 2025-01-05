n = int(input())
score = list(map(int, input().split()))
max_num = max(score)
avg = sum(score) / max_num * 100

print(avg / n)