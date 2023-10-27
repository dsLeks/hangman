import random
from hangman_art import stages, logo
from hangman_words import word_list



#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')

display = []
for i in range(0, len(chosen_word)):
    display.append("_")

while("_" in display):
    guess = input("Guess a letter: ").lower()
    
    if guess in chosen_word:
        print("You guessed " + guess)
        for x in range(0, len(chosen_word)):
            if(chosen_word[x] == guess):
                display[x] = guess
        print(display)
        print(stages[lives])
    else:
        print("You guessed " + guess + " but it's not in the word!")
        lives -= 1
        print(display)
        print(stages[lives])
        if(lives == 0):
            print("You Lose!")
            break

        
if("_" not in display):
    print("Congrats! You Win!")          
            