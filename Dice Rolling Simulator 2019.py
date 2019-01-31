import time

turnsLeft = 100
while turnsLeft > 0:
    print('Welcome to Dice Rolling Simulator 2019')

    import random
    dicenum1 = random.randint(1,6)
    dicenum2 = random.randint(1,6)
    dicenum3 = random.randint(1,6)
    dice1 = str(dicenum1)
    dice2 = str(dicenum2)
    dice3 = str(dicenum3)
    diceSum2 = str(dicenum1 + dicenum2)
    diceSum3 = str(dicenum1 + dicenum2 + dicenum3)

    print('How many dice would you like to roll?')
    print('1')
    print('2')
    print('3')

    choice = (input('Enter number(1/2/3): '))

    if choice == '1':
        print('Rolling now...')
        time.sleep(1)
        print('You rolled a ' + dice1 + '!')
        time.sleep(1)
        turnsLeft = turnsLeft - 1
        print('You have ' + str(turnsLeft) + ' turns left! Press enter to continue.')
        input()
    elif choice == '2':
        print('Rolling now...')
        time.sleep(1)
        print('The first number rolled is ' + dice1 + '!')
        time.sleep(1)
        print('And the second is ' + dice2 + '!')
        time.sleep(1)
        print('This means in total you rolled ' + diceSum2 + '.')
        time.sleep(1)
        turnsLeft = turnsLeft - 1
        print('You have ' + str(turnsLeft) + ' turns left! Press enter to continue.')
        input()
    elif choice == '3':
        print('Rolling now...')
        time.sleep(1)
        print('The first number rolled is ' + dice1 + '!')
        time.sleep(1)
        print('And the second is ' + dice2 + '!')
        time.sleep(1)
        print('The third is ' + dice3 + '!')
        time.sleep(1)
        print('This means in total you rolled ' + diceSum3 + '.')
        time.sleep(1)
        turnsLeft = turnsLeft - 1
        print('You have ' + str(turnsLeft) + ' turns left! Press enter to continue.')
        input()
    else:
        print('Error!')
        print('Aborting program')
        time.sleep(3)
        turnsLeft = 0

   
    



