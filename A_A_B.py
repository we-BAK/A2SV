n = int(input())
for _ in range(n):
    expression = input()     
    a, b = expression.split('+')  
    result = int(a) + int(b)      
    print(result)
