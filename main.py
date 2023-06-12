#Hangman Game
import random
from Stages import stages
from Words import word_list
#Main Section-------------------------------------------------------------

random_word = random.choice(word_list)

length = len(random_word)


def check(): #Checks if the condition is met.
    """Checks if a certain condition is met."""
    counter = display.count('_')
    return counter == 0

#Code Area
display = ['_']*length

print(f"{''.join(display)}")

lives = 7

while check() == False and lives > 0:

    guess = input("Guess a letter: ").lower()

    lost_life = True

    if not guess.isalpha():
        print("Please enter a valid letter.")

    elif display.count(guess) != 0:
        print('This has been already guessed.')
    
    else:
        for position in range(length):
            letter = random_word[position]

            if letter == guess:

                display[position] = guess
                lost_life = False

        if lost_life == True:
            lives -= 1
            print("The letter isn't included in choosen word. Lost a life.")
            print(stages[lives])

        print(f"{''.join(display)}\n")

if lives == 0:
    print(f"You lost! The word was {random_word}.")
else:
    print("You won!")
