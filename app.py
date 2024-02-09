# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
# If both players choose the same, it's a tie.
# # The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random

def game():
    player_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        player = input("Enter rock, paper, or scissors: ").lower()
        computer = random.choice(["rock", "paper", "scissors"])
        if player not in ["rock", "paper", "scissors"]:
            print("Invalid option. Please enter rock, paper, or scissors.")
            continue
        print(f"Computer chose {computer}.")
        if player == computer:
            print("It's a tie!")
        elif player == "rock":
            if computer == "scissors":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player == "scissors":
            if computer == "paper":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player == "paper":
            if computer == "rock":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        print(f"Player: {player_score} | Computer: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print(f"Final score: Player: {player_score} | Computer: {computer_score}")

if __name__ == "__main__":
    game()