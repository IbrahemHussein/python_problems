def distinct_letters():
    anto_set = input()
    letters = [i for i in anto_set if i != '{' and i != '}' and i != ' ' and i != ',']

    unique_letter = []
    for letter in letters:
        if letter not in unique_letter:
            unique_letter.append(letter)
    print(len(unique_letter))


distinct_letters()

