def beautiful_year():
    year = int(input())
    year += 1
    while len(set(str(year))) != len(str(year)):
        year += 1
    print(year)


if __name__ == "__main__":
    beautiful_year()
