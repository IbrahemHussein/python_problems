def differs():
    s = input()
    main_str = 'codeforces'
    total = 0
    for i, j in zip(s, main_str):
        if i != j:
            total += 1
    print(total)
    return


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        differs()
