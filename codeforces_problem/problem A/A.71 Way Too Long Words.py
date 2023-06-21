def long_words():
    text = input()
    center = text[1:-1]
    if len(text) <= 10:
        print(text)
    else:
        print(f'{text[0]}{len(center)}{text[-1]}')


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        long_words()
