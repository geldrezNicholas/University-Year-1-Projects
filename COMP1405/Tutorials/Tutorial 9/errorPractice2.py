def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'Division by zero is not allowed.'
    
def main():
    flag = True
    while flag:
        a = input('Enter the first number (a): ')
        b = input('Enter the second nunber (b): ')
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print('Invalid input, please enter numeric values.')
    print(f'Result: {safe_divide(a,b)}')
    quit = input('Do you want to perform another calculation? (type "quit" to exit): ')
    if quit == 'quit':
        flag = False
    else:
        flag = True

main()