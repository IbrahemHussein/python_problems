def domino_piling():
    """the function used to  Find the maximum number of dominoes, which can be placed under these restrictions.
    """
    n,m=map(int,input().split())
    total=(n*m)/2
    print(int(total))
    return


if __name__ == '__main__':
    domino_piling()