def problem_search():
    num = int(input())
    problems = list(map(int, input().split(' ')))
    if 1 in problems:
        print('HARD')
    else:
        print('EASY')


problem_search()
