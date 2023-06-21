def min_to_divisible():
    num = int(input())
    result = []
    for _ in range(num):
        a, b = map(int, input().split(' '))
        if a % b == 0:
            result.append(0)
        else:
            result.append(b - a % b)
    for i in result:
        print(i)


min_to_divisible()
