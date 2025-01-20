m = int(input())
n = int(input())

prime_list = []

for num in range(m, n + 1):
    if num < 2:
        continue
    
    is_prime = True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        prime_list.append(num)

if prime_list:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print(-1)