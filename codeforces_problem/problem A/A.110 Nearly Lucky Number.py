def is_nearly_lucky():
    number = input()
    count = 0
    for digit in number:
        if digit in ['4','7'] :
            count += 1
    if count in [4, 7]:
        print('YES')
    else:
        print('NO')


is_nearly_lucky()
