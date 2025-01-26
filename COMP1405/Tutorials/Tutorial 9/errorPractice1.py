def convert_to_int(myString):
    try:
        newInt = int(myString)
    except ValueError:
        return 'Invalid input'
    return newInt

def main():
    x = 0
    while x < 3:
        integer = input('Enter an integer: ')
        print(convert_to_int(integer))
        x += 1

main()
    