t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    color = {}
    for i, x in enumerate(sorted(a)):
        color[x] = i % 2
    
    ok = True
    for i in range(1, n):
        if color[a[i]] == color[a[i-1]]:
            ok = False
            break
    if ok :
        print("YES" )
    else :
        print("NO")
