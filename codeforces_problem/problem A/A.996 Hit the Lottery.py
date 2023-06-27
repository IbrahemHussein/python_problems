def min_of_bills():
    number = int(input())
    c100 = c20 = c10 = c5 = c1 = 0
    c100 = number // 100
    number = number % 100
    c20 = number // 20
    number = number % 20
    c10 = number // 10
    number = number % 10
    c5 = number // 5
    number = number % 5
    c1 = number
    total = c100 + c10 + c5 + c1+c20
    return total


print(min_of_bills())
