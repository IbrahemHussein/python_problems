def minimum_coins():
    num = int(input())
    num_coins = list(map(int, input().split(' ')))
    average_coins = sum(num_coins) / 2
    num_coins.sort(reverse=True)
    for i in range(len(num_coins)):
        my_coins = num_coins[:i+1]
        if sum(my_coins) > average_coins:
            print(len(my_coins))
            break


minimum_coins()
