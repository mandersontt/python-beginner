#Hangman Game v2
import time
import random
import sys

loopCode = 1
while loopCode == 1:

    def closeApplication():
        print('Application closing in:')
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        sys.exit()

    def mainMenu():
        print('-' * 30)
        print('Welcome to hangman!')
        print('Would you like to play?')
        playResponse = input('(Y/N): ')
        print('')
        playResponse = playResponse.upper()
        if playResponse == 'Y':
            time.sleep(1)
        elif playResponse == 'N':
            closeApplication()
        else:
            print('Unrecognised response! Application closing')
            closeApplication()

    def rePlay():
        print('Would you like to return to the main menu?')
        playResponse = input('(Y/N): ')
        print('')
        playResponse = playResponse.upper()
        if playResponse == 'Y':
            time.sleep(1)
        elif playResponse == 'N':
            closeApplication()
        else:
            print('Unrecognised response! Application closing')
            closeApplication()

    mainMenu()
            
    def getGuess():
        hiddenAnswer = "?" * len(secretWord)
        guessesRemaining = 10
        while guessesRemaining > 0 and not hiddenAnswer == secretWord:
            print('Your word to guess is: ' + hiddenAnswer)
            print('')
            print('You have ' + str(guessesRemaining) + ' guesses left!')
            print('Your word is ' + str(len(secretWord)) + ' letters long.')
            time.sleep(1)
            print('')
            guess = input('Please guess a letter: ')
            print('')
            guess = guess.lower()
            if len(guess) != 1:
                print('Please ensure guess is one character.')
                print('')
            elif guess in secretWord:
                print('')
                print('Well done! Letter guessed correctly.')
                print('')
                hiddenAnswer = updateHiddenAnswer(secretWord, hiddenAnswer, guess)
            else:
                guessesRemaining = guessesRemaining - 1
                print('Incorrect guess!')
                print ('')
        if guessesRemaining <= 0:
            print('You lose. The word was: ' + str(secretWord) + '.')
            print('')
            time.sleep(1)
            rePlay()
        else:
            print('Congratulations! You were right, the hidden word was: ' + str(secretWord) + '.')
            print('')
            time.sleep(1)
            rePlay()

    def updateHiddenAnswer(secret, curDash, recGuess):
        result = ''

        for i in range(len(secret)):
            if secret[i] == recGuess:
                result = result + recGuess
            else:
                result = result + curDash[i]
        return result

    wordList = ['dolphin', 'shark', 'whale', 'fish', 'porpoise', 'penguin']

    secretWord = random.choice(wordList)
    getGuess()
            
                
            
