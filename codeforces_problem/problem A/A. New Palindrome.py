def panlindromr():
    s = input().strip()
    n = len(s)
    for i in range(n // 2 - 1):
        if s[i] != s[i + 1]:
            print('YES')
            return
    print('NO')


if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        panlindromr()
