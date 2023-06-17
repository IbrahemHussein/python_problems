def tram():
    num = int(input())
    total = 0
    capacity = 0
    for i in range(num):
        a, b = map(int, input().split())
        total -= a
        total += b
        if total > capacity:
            capacity = total
    return capacity

if __name__ == '__main__':
    print(tram())