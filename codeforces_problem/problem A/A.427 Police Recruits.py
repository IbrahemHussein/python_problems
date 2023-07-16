free_officers = 0
untreated_crimes = 0
num = int(input())
events = map(int, input().split((' ')))

for i in events:
    if i < 0:
        if free_officers >0:
            free_officers -= 1
        else:
            untreated_crimes += 1
    elif i > 0:
        free_officers += i
print(untreated_crimes)


