import random

print('Hello. What is your name? ')
name = input()

print('Well,' + name + 'I am thinking of a number between 1 and 20. Try to guess it. ')
secretNumber = random.randint(1, 20)

for guessesTaken in range (1, 7):
    print('Take a guess. ')
    guess = int(input())
    try:
        if guess < secretNumber:
            print('Too low buddy. Try it again. ')
        elif guess > secretNumber:
            print('Too high buddy. Try it again. ')
        elif guessesTaken == 7:
            print('you have tryed enough. Thanks for playing.')
        elif guess == secretNumber:
            print('Congratulations, you guessed the correct number. ')
            break
    except ValueError:
        print('That is not a number. Try it again. ')

print('Thanks for playing! ')

        
