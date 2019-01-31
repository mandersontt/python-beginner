#Maze Concept
#Top left - A1
#Top right - A2
#Bottom left - B1
# A1|A2
# -----
# B1|

import time
import sys

def setVar():
    global inventory, doorKey, sword, buttonClicked
    inventory = ''
    doorKey = 'Door Key'
    sword = 'Sword'
    buttonClicked = 0

setVar()

def getKey():
    global inventory
    global doorKey
    inventory = inventory + doorKey

def getSword():
    global sword
    global inventory
    inventory = inventory + sword

def b1start():
    print('You awaken in a dark cell, your vision returns as you sit up on the old bed.')
    time.sleep(1)
    print('You have no memory of how you got here.')
    time.sleep(2)
    print('')
    b1menu()

def b1menu():
    print('What would you like investigate?')
    print('1. Cell door')
    print('2. Chest')
    print('3. Bed')
    print('')
    b1inv = input('Please select an option (1/2/3): ')
    print('')
    if len(b1inv) != 1:
        print('Please ensure your choice is one character.')
        print('')
        b1menu()
    elif int(b1inv) >= 4:
        print('Please choose between options (1/2/3).')
        print('')
        b1menu()
    elif b1inv == '1':
        b1inv1()
    elif b1inv == '2':
        time.sleep(1)
        print('You find nothing!')
        print('')
        time.sleep(1)
        b1menu()
    elif b1inv == '3':
        b1inv3()
    else:
        time.sleep(1)
        print('Invalid entry!')
        print('')
        time.sleep(1)
        b1menu()

def b1inv3():
    if doorKey not in inventory:
        time.sleep(1)
        print('You search under the bed...')
        print('')
        time.sleep(1)
        print('You find a key!')
        time.sleep(1)
        print('')
        getKey()
        print('*Door Key added to inventory*')
        print('')
        time.sleep(1)
        b1menu()
    else:
        time.sleep(1)
        print('You search under the bed...')
        time.sleep(1)
        print('You already found the key!')
        time.sleep(1)
        print('')
        b1menu()      

def b1inv1():
    if doorKey not in inventory:
        time.sleep(1)
        print('You investigate the cell door...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('')
        print('The door is locked!!!')
        print('')
        time.sleep(1)
        b1menu()
    else:
        print('You unlock the cell door with the door key!')
        time.sleep(1)
        print('You move out of your cell and into the room to the north')
        print('')
        time.sleep(1)
        a1enter()

def a1enter():
    print('You walk into the room and see a guard facing the other way.')
    time.sleep(1)
    print('')
    print('There is a sword on the table, if you take it you can defeat the guard!')
    time.sleep(1)
    print('')
    a1menu()

def a1menu():
    print('What would you like to do?')
    print('1. Pick up sword')
    print('2. Attack guard')
    print('')
    a1sel = input('Please choose an action (1/2): ')
    print('')
    time.sleep(1)
    if len(a1sel) != 1:
        print('Please ensure your choice is one character.')
        print('')
        time.sleep(1)
        a1menu()
    elif int(a1sel) >= 3:
        print('Please choose between options (1/2/3).')
        print('')
        time.sleep(1)
        a1menu()
    elif a1sel == '1':
        print('You pick up the sword!')
        time.sleep(1)
        print('*Sword added to inventory*')
        time.sleep(1)
        print('')
        getSword()
        print('Now that you have the sword you attack the guard!')
        print('')
        attackGuard()
    elif a1sel == '2':
        attackGuard()
    else:
        print('Invalid entry!')
        print('')
        time.sleep(1)
        a1menu()

def attackGuard():
    if sword not in inventory:
        time.sleep(1)
        print('You go to attack the guard...')
        print('')
        time.sleep(1)
        print('As you are unarmed, the guard retalliates and knocks you out!')
        time.sleep(1)
        print('')
        b1start()
    else:
        print('You attack the guard...')
        time.sleep(1)
        print('You overpower him! He is knocked out.')
        print('')
        time.sleep(1)
        print('You move past him to the room to the east.')
        print('')
        a2enter()

def a2enter():
    time.sleep(1)
    print('You walk into a room lined with four statues with a grand door at the end.')
    print('')
    time.sleep(1)
    a2menu()

def a2menu():
    print('What would you like to do?')
    print('1. Investigate the northwest statue')
    print('2. Investigate the southwest statue')
    print('3. Investigate the northeast statue')
    print('4. Investigate the southeast statue')
    print('5. Try and open the door')
    print('')
    time.sleep(1)
    a2sel = input('Select an option (1/2/3/4/5): ')
    print('')
    if len(a2sel) != 1:
        print('Please ensure your choice is one character.')
        print('')
        time.sleep(1)
        a2menu()
    elif int(a2sel) >= 6:
        print('Please choose between options (1/2/3).')
        print('')
        time.sleep(1)
        a2menu()
    elif a2sel == '1':
        print('You search the statue...')
        time.sleep(1)
        print('You find nothing.')
        print('')
        time.sleep(1)
        a2menu()
    elif a2sel == '2':
        print('You search the statue...')
        time.sleep(1)
        print('You find nothing.')
        print('')
        time.sleep(1)
        a2menu()
    elif a2sel == '3':
        buttonStatue()
    elif a2sel == '4':
        print('You search the statue...')
        time.sleep(1)
        print('You find nothing.')
        print('')
        time.sleep(1)
        a2menu()
    elif a2sel == '5':
        time.sleep(1)
        print('You walk up to the grand door at the end of the room...')
        print('')
        time.sleep(1)
        openDoor()
    else:
        time.sleep(1)
        print('Invalid entry!')
        print('')
        a2menu()

def openDoor():
    global buttonClicked
    print('You see that the door has a large handle and attempt to open it...')
    print('')
    time.sleep(1)
    if buttonClicked == 0:
        print('It will not open, must be locked!')
        print('')
        time.sleep(1)
        a2menu()
    else:
        print('The door slowly opens up... you cannot believe what you see inside...')
        time.sleep(1)
        print('')
        print(' It-')
        print('')
        time.sleep(1)
        print('It canno-')
        print('')
        time.sleep(1)
        print('It cannot be!')
        print('')
        time.sleep(1)
        print('It is! Its...')
        time.sleep(1)
        print('')
        print('Deez Nuts!')
        time.sleep(30)
        sys.exit()

def buttonStatue():
    global buttonClicked
    if buttonClicked == 0:
        print('You search the statue...')
        time.sleep(1)
        print('You notice a button hidden behind it...')
        time.sleep(1)
        print('You press the button!')
        print('')
        time.sleep(1)
        print('*Click!*')
        buttonClicked = 1
        print('')
        time.sleep(1)
        a2menu()
    else:
        print('You search the statue...')
        time.sleep(1)
        print('You have already pressed the button!')
        print('')
        a2menu()


b1start()
