password = input()
n = int(input())

found_first = False
found_second = False

for _ in range(n):
    s = input()
    
    if s == password:
        print("YES")
        exit()
    
    if s[0] == password[1]:
        found_first = True
    if s[1] == password[0]:
        found_second = True

if found_first and found_second:
    print("YES")
else:
    print("NO")
