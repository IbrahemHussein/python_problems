# Todo:Write A Python Program To Take Age From The User To Check Whether User Able To Participate In Voting Or Not.
#  If Age Is Less Than 18 Then It Don’t Allow To Participation.
#  And Show, After How Much Year A Person Will Be Able To Participate:

user_age = int(input('enter yor age :'))
if user_age >= 18:
    print('You can participate in voting, ')
else:
    print(f'Sorry! You cannot participate in voting, you will be able to participate after {18 - user_age} year')


# part two: Assignment
# Todo:Write A Python Program To Take Marks From The User To Check Whether User Able To Admission In College Or Not.
#  If Marks Is Less Than 60 Then It Don’t Allow To Take Admission.
#  Expected Result if user input 50 year then:
#  Sorry! You cannot take admission, you need 10 numbers more to take admission

user_marks = int(input('enter your marks :'))
if user_marks >= 60:
    print('You can take admission')
else:
    print(f'Sorry! You cannot take admission, you need {60 - user_marks} numbers more to take admission')
