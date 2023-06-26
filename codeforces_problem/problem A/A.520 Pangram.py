# Todo: import string that contain alphabet characters
import string


# Todo: make a function that returns if string is pangram
def is_a_pangram(n, word):
    # todo: check if string is pangram
    alphabet = string.ascii_lowercase
    if len(word) == n:
        unique_letters = ''.join(sorted(set(word.lower())))
        if unique_letters == alphabet:
            return True
        else:
            return False


# Todo: make user input the number of the characters
num = int(input())
# Todo: make user input the string
user_string = input().lower()
if is_a_pangram(num, user_string):
    print('YES')
else:
    print('NO')
