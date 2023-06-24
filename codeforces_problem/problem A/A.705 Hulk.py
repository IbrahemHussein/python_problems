def Dr_Banner_feeling():
    num = int(input())
    felling = 'I hate'
    for i in range(2, num + 1):
        if i % 2 == 0:
            felling += ' that I love'
        else:
            felling += ' that I hate'
    felling += ' it'
    return felling

print(Dr_Banner_feeling())
