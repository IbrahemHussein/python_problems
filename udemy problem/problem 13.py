# ToDo: Write Python Program To Get Password From User And Make Sure That Password Should Contain
#  Number And Alphabetic AND Password Length Should Not Be Greater Than Or Equal To 8

#step1: Get Password From the User
password = input("Enter Password")
if password.isalnum():
    if len(password)<=8:
        print(f'your password : {password} is okey')
    else:
        print(f'your password : {password} is too long try again' )
else:
    print(f'sorry ,we didn\'t allow while space and special char in your password {password} ')


