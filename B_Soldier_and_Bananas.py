k, n, w = map(int, input().split())

total_cost = 0

for i in range(1, w + 1):
    total_cost += i * k

money_needed = total_cost - n
print(money_needed)
