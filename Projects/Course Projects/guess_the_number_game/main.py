#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

def ans_check(actual_num, guessed_num):
    if guessed_num > actual_num:
        return "Too high!"
    elif guessed_num < actual_num:
        return "Too low!"
    else:
        return "Correct Answer!"


print("Welcome to the number guessing game.")

actual_num = random.randint(1, 100)
game_level = input("Enter the difficulty level: ").lower()

if game_level == "easy":
    turns = 10
elif game_level == "medium":
    turns = 7
elif game_level == "hard":
    turns = 5
else:
    turns = 0
    print("Invalid Input.")

while turns != 0:
    print(f"You have {turns} turns left!")
    guessed_num = int(input("Guess a number between 1 to 100: "))
    ans = ans_check(actual_num, guessed_num)

    if ans == "Correct Answer!":
        turns = 0
        print(ans)
    else:
        turns -= 1
        print(ans)
        if turns == 0:
            print("You have lost all the turns!")
