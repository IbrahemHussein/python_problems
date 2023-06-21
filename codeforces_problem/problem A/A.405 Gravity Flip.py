def gravity_switch():
    num = int(input())
    boxes = list(map(int, input().split(' ')))
    result = ' '.join(map(str, sorted(boxes)))
    return result


print(gravity_switch())
