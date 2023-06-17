def Consonants():
    string=input().lower()
    new_string=''
    vowels=["a", "o", "y", "e", "u", "i"]
    for i in string:
        if   i not in vowels:
            new_string+='.'+i
    return new_string

if __name__ == "__main__":
    print(Consonants()) 