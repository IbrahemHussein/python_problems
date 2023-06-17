def event_adds():
    n, k = map(int, input().split())
    flag = int((n + 1) / 2)
    if k <= flag:
        print(int((k * 2) - 1))
    else:
        print(int((k - flag) * 2))


event_adds()

