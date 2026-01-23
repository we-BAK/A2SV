def swap_case(s):
    string=[]
    for letter in s:
        if letter.isupper():
            string.append(letter.lower())
        else:
           string.append(letter.upper())
    return "".join(string)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)