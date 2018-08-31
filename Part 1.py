__author__ = 'Dreyke Boone'

# import random module
import random

# keep track of user guesses
userGuesses = 0
number = random.randint(1, 30)
print("Guess a number between 1 and 30. Choose wisely, you only get 5 chances.. ")

#
while userGuesses < 5:
    print("Take a guess")
    guess = input()
    guess = int(guess)

    userGuesses = userGuesses + 1

    if guess < number:
        print("Too low")

    if guess > number:
        print("Too high")

    if guess == number:
        break

if guess == number:
    userGuesses = str(userGuesses)
    print("Good job! You guessed my number in " + userGuesses + " guesses." )

if guess != number:
    number = str(number)
    print("Sorry. The number I was thinking of is " + number)