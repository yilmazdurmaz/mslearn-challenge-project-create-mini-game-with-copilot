# write "hello world" to the console
print("hello world")  # this should have been filled by CoPilot

# specs for copilot
# -Rock beats scissors.
#- Scissors beat paper.
#- Paper beats rock.
# -The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# -At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# -By the end of each round, the player can choose whether to play again.
# -Display the player's score at the end of the game.
# -The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
# PROMPT: use it as a specification sheet to create a python program

import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    options = ['rock', 'paper', 'scissors']
    score = {'player': 0, 'computer': 0, 'tie': 0}
    while True:
        print(f"\nScore: Player {score['player']} - Computer {score['computer']} - Tie {score['tie']}")
        user_choice = input("Enter your choice: 'rock', 'paper', or 'scissors' (or 'quit' to exit): ").lower()
        if user_choice == 'quit':
            break
        elif user_choice not in options:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue
        computer_choice = random.choice(options)
        print(f"\nYou chose {user_choice}, and the computer chose {computer_choice}.\n")
        if user_choice == computer_choice:
            print("It's a tie!")
            score['tie'] += 1
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            score['player'] += 1
        else:
            print("The computer wins!")
            score['computer'] += 1
    print(f"\nFinal score: Player {score['player']} - Computer {score['computer']} - Tie {score['tie']}")
    print("\nThanks for playing!")

play_game()