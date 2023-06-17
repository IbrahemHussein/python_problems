def a_add_b():
    text = input()
    a = int(text[0])
    b = int(text[-1])
    if a <= 9 and b <= 9:
        print(a + b)
        return


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a_add_b()
