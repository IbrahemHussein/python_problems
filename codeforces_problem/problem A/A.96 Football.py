def is_dangers():
    text = input()
    total = 1
    for i in range(len(text)-1):
        if text[i] == text[i + 1]:
            total += 1
            if total == 7:
                print('YES')
                break
        else:
            total = 1
    else:
        print('NO')


if __name__ == '__main__':
    is_dangers()
