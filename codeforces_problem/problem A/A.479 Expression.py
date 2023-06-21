def maximum_expression():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    return max(n1 + n2 * n3, n1 * (n2 + n3), n1 * n2 * n3, (n1 + n2) * n3,n1+n2+n3)


print(maximum_expression())
