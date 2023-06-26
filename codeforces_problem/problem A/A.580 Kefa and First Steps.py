def min_non_decreasing():
    num = int(input())
    numbers = list(map(int, input().split(' ')))
    lenght = 1
    max_lenght = 1
    for i in range(1, num):
        if numbers[i] >= numbers[i - 1]:
            lenght += 1
        else:
            max_lenght = max(max_lenght, lenght)
            lenght = 1

    max_lenght = max(max_lenght, lenght)
    print(max_lenght)


min_non_decreasing()
