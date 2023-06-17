def magnets():
    num = int(input())
    magnet_list = [input() for i in range(num)]
    count = 1

    for i in range(len(magnet_list) - 1):
        f1 = magnet_list[i]
        f2 = magnet_list[i + 1]
        if f1[-1] != f2[-1]:
            count += 1
    if count < 1:
        print(len(magnet_list))
    else:
        print(count)
magnets()