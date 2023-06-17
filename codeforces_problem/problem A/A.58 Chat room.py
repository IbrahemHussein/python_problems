

def can_say_hello():
    string=input()
    hello = "hello"
    i = 0  # pointer for hello
    j = 0  # pointer for s
    while i < len(hello) and j < len(string):
        if hello[i] == string[j]:
            i += 1
        j += 1
    return i == len(hello)

if can_say_hello():
    print("YES")
else:
    print("NO")