def is_equilibrium():
    """
    Checks if the equilibrium condition is satisfied.
    """
    num = int(input())
    vectors = []
    for i in range(num):
        vectors.append(list(map(int, input().split())))
    sum_vector = [sum(x) for x in zip(*vectors)]
    if sum_vector == [0, 0, 0]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    is_equilibrium()
