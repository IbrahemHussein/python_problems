def team():
    total = 0
    for _ in range(t):
        answer = input().split(' ')
        n1 = int(answer[0])
        n2 = int(answer[1])
        n3 = int(answer[2])
        if (n1 + n2 + n3) >= 2:
            total += 1
    print(total)
    return


if __name__ == "__main__":
    #t = int(input())
    #team()
    import math
    x=(math.ceil(6/4))*(math.ceil(6/4))
    print(x)