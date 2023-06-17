def zero_one_digit():
    n1 = input()
    n2 = input()
    result_list = []
    if len(n1) == len(n2) and len(n1) <= 100 and len(n2) <= 100:
        for i, j in zip(n1, n2):
            if i == j:
                result_list.append('0')
            else:
                result_list.append('1')
    print("".join(result_list))


zero_one_digit()
