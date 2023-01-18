num = int(input('Enter an integer greater than 1: '));
x = 0
while x <= num:
    print ('The cube of ' + str(x) + ' is ', end='' )
    print(x**3)
    x = x + 1
