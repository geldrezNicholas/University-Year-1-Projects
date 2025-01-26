a = int(input('1:'))
b = int(input('2:'))
c = int(input('3:'))

if((a+b > c) and (b+c>a) and (a+c>b)):
    print('This is a triangle.')
else:
    print('This is not a triangle.')