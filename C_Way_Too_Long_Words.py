n = int(input())
for _ in range(n):
    word = input()

    if len(word) > 10:
        short_word = word[0] + str(len(word) - 2) + word[-1]
        print(short_word)
    else:
        print(word)
