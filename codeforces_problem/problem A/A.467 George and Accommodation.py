def empty_room():
    num = int(input())
    room_list = []
    for _ in range(num):
        room = list(map(int, input().split(' ')))
        room_list.append(room)
    count_room = 0
    for i, j in room_list:
        if abs(i - j) >= 2:
            count_room += 1
    print(count_room)


empty_room()
