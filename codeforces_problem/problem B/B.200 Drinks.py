def orange_percentage():
    num = int(input())
    juices = list(map(int, input().split(' ')))
    result = float(sum(juices) / num)
    print(f'{result:f}')


orange_percentage()
