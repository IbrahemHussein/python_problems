def min_horseshoes():
    number = set(map(int, input().split()))
    return 4 - len(number)


print(min_horseshoes())
