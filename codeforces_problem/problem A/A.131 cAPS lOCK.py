def caps_lock():
    word=input()
    if word.isupper():
        return word.lower()
    elif len(word)==1:
        return word.upper()
    elif word[0].islower() and word[1:].isupper():
        return word.capitalize()
    else:
        return word
print(caps_lock())