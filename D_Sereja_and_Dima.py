n = int(input())
cards = list(map(int, input().split()))
i = 0
j = n - 1
serja = 0
dima = 0
turn = 0
while i <= j:
    if cards[i] >= cards[j]:
        pick = cards[i]
        i += 1
    else:
        pick = cards[j]
        j -= 1
    
    if turn % 2 == 0:
        serja += pick
    else:
        dima += pick
    turn += 1
print(serja, dima)