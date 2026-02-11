for _ in range(int(input())):
    arr=list(map(int,input().split()))
    target=max(arr)
    arr.remove(target)
    if sum(arr)==target:
        print("YES")
    else:
        print("NO")
    