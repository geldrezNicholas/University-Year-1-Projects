#   COMP 1405 Section C - Assignment 1 Program 1
#    Project Details
#       Name: Nicholas Geldrez
#       Date Created: September 27, 2024

inputMessage = input('Type your message here:')
shift = int(input('How far do you want to shift your message(1-5)?'))

capsMessage = inputMessage.upper()
encodedMessage = ''

for e in capsMessage:
    character = (ord(e[:1:])) #Slices the first character and turns it to decimal through ASCII
    if(int(character) >= 65 and int(character) <= 90): #checks if character is a letter
        if ((character + shift) > 90): #if the character passes 'Z', return it to 'A', continue shift
            encodedMessage += chr(character - 26 + shift) 
        else:
            encodedMessage += chr(character + shift)
    else: 
        encodedMessage += chr(character)  #adds character to final message
print(f'Your encoded message is:{encodedMessage}')