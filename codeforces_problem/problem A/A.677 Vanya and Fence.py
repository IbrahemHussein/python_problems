def width_road():
    n, h = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    total = 0
    for i in a:
        if i <= h:
            total += 1
        else:
            total += 2
    print(total)


if __name__ == "__main__":
    width_road()
