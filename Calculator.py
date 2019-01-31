import time

loopCode = 1

while loopCode == 1:

    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y

    print('Select Operation.')
    time.sleep(0.5)
    print('1.Add')
    print('2.Subtract')
    print('3.Multiply')
    print('4.Divide')
    print('')
    time.sleep(0.5)
    choice = input('Enter Choice(1/2/3/4): ')
    time.sleep(0.5)
    num1 = int(input('Enter first number: '))
    time.sleep(0.5)
    num2 = int(input('Enter second number: '))
    time.sleep(0.5)
    print('')

    if choice == '1':
        print(num1, '+', num2, '=', add(num1,num2))
    elif choice == '2':
        print(num1, '-', num2, '=', subtract(num1, num2))
    elif choice == '3':
        print(num1, '*', num2, '=', multiply(num1, num2))
    elif choice == '4':
        print(num1, '/', num2, '=', divide(num1, num2))
    else:
        print('Invalid Input!')

    time.sleep(1)
    print('Would you like to perform another function?')
    continueResponse = input('(Y/N): ')

    if continueResponse == 'N':
        print('Application closing in 3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        loopCode = 0,
    elif continueResponse == 'n':
        print('Application closing in 3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        loopCode = 0,
    else:
        time.sleep(1)
        print('')
