def subtraction():
    text = input().split()
    n = text[0]
    k = int(text[1])
    for i in range(k):

        if n[-1] == '0':
            new_n = int(int(n) / 10)

        else:
            new_n = int(n) - 1
        n = str(new_n)
    return int(new_n)


if __name__ == '__main__':
    print(subtraction())
