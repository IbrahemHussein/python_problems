def Calculating():
    n = int(input())
    if n % 2 == 0:
        print((-1) ** n * (n // 2))
    else:
        print((-1) ** n * ((n + 1) // 2))


Calculating()
