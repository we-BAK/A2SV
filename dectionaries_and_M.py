import sys

n = int(sys.stdin.readline().strip())

phone_book = {}

for _ in range(n):
    entry = sys.stdin.readline().split()
    name = entry[0]
    phone = entry[1]
    phone_book[name] = phone
for query in sys.stdin:
    name = query.strip()
    
    if name in phone_book:
        print(f"{name}={phone_book[name]}")
    else:
        print("Not found")