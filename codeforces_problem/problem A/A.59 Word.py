def word():
    string = input()
    num_upper = 0
    num_lower = 0
    for letter in string:
        if letter.isupper():
            num_upper += 1
        else:
            num_lower += 1
    if num_upper <= num_lower:

        print(string.lower())
    else:
        print(string.upper())


if __name__ == '__main__':
    word()
