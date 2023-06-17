def compare_string():
    #ToDo: first we need to input the string1 and the string2
    s1,s2=input().lower(),input().lower()

    #ToDo:compare between the two strings
    if s1==s2:
        return 0
    for i in range (len(s1)):
        #If the first string is less than the second one, print "-1"
        if s1[i]<s2[i]:
            return -1
        #If the second string is less than the first one, print "1".
        elif s1[i]>s2[i]:
            return 1
        # If the strings are equal, print "0". 
        
    
    
if __name__ == "__main__":
    print(compare_string())