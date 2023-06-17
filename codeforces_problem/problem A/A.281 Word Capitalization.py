def capital():
    """function take a string and return a capitalized string"""
    #ToDo: input string  
    string=input()
    #ToDo: capitalize the first character and return it 
    return string[0].upper() + string[1:]
if __name__ == "__main__":
    print(capital())