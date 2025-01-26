#   COMP 1405 Section C - Assignment 1 Program 1
#    Project Details
#       Name: Nicholas Geldrez
#       Date Created: September 27, 2024

userValue = float(input('Input your score between 0.0 and 1: '))
if(userValue >= 0.9 and userValue <= 1):#1st Grade
    print('You got an A!')
elif(userValue >= 0.8 and userValue < 0.9):#2nd Grade
    print('You got a B!')
elif(userValue >= 0.7 and userValue < 0.8):#3rd Grade
    print('You got a C!')
elif(userValue >= 0.6 and userValue < 0.7):#4th Grade
    print('You got a D!')
elif(userValue < 0.6 and userValue >= 0):#5th Grade
    print('You got a F!')
else:#Above or below score range
    print('This is not a score!')