import pygame

#Colours
white = (255,255,255)
black = (0,0,0)
brown = (139,69,19)

#Display
x = pygame.display.set_mode((400,400))
x.fill(white)

#Grid
for e in range(20):
    pygame.draw.line(x, black, (20*e,0), (20*e,400))
    pygame.draw.line(x, black, (0,20*e), (400,20*e))

#Smiley
smile = input('Input "s" for smile or "f" for frown: ')
if (smile == 's'):
    pygame.draw.arc(x, black, [(150,220),(100,50)], 3, 0, 4)
elif(smile == 'f'):
        pygame.draw.arc(x, black, [(150,220),(100,50)], 0, 3, 4)   
else:
    print('Choose an option') 
pygame.draw.circle(x, black, (200,200), 100, 3)
pygame.draw.circle(x, brown, (160,170), 10, 0)
pygame.draw.circle(x, brown, (240,170), 10, 0)

#Display
pygame.display.update()
pygame.time.delay(5000)