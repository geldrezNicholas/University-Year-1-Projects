import random

r = random.randint(1,100)

print('Welcome to the guessing game! You have 10 attemps to guess the number.')
for e in range(1,11):
    i = int(input(f'Attempt #{e}: Guess a number between 1 and 100:'))
    if (i == r):
        print(f'You are correct the number was {r}.')
        break
    elif(i > r):
        print(f'Your guess was too high.')
        if(e == 10):
            print(f'The number was {r}.')
    else:
        print(f'Your guess was too low.')
        if(e == 10):
            print(f'The number was {r}.')