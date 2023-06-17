def main_step_to_friend():
    x = int(input())
    if x < 5:
        return 1
    elif x % 5 == 0:
        return x // 5
    else:
        return x // 5 + 1


if __name__ == '__main__':
    print(main_step_to_friend())
