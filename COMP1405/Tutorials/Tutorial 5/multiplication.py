user = int(input('Enter a number (1-9): '))
for e in range(1, user+1):
    for i in range(1, user+1):
        print(e * i, end='\t')
    print()