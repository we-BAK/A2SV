t= int(input())
for _ in range(t):
  n, s, x = map(int, input().split())
  arr = list(map(int, input().split()))
  sum1  = sum(arr)
  if sum1 <= s and (sum1 - s) % x == 0:
    print("YES")
  else:
    print("NO")