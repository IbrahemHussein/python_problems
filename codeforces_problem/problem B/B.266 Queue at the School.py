def school_queue():
    n, t = map(int, input().split((' ')))
    string = list(input())
    for i in range(t):
        j = 0
        while j < n - 1:
            if string[j] == 'B' and string[j + 1] == 'G':
                string[j], string[j + 1] = string[j + 1], string[j]
                j += 2
            else:
                j += 1

    print(''.join(string))


if __name__ == "__main__":
    school_queue()
