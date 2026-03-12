# If someone want then he fix the game to cheat only one thing we need to do some changes

import random

print("Hey, Lets's play Rock, paper, scissors")

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

player = input("Enter your choice: ").lower()

print(f"you chose: {player} \n computer chose: {computer}")

if (player == computer):
    print("It's a tie!!")

elif(player == "rock" and computer == "scissors"):
    print("You win!")

elif(player == "paper" and computer == "rock"):
    print("You win!")

elif(player == "scissors" and computer == "paper"):
    print("You win!")

elif(player == "rock" and computer == "paper"):
    print("You lose!!")

elif(player == "scisors" and computer == "rock"):
    print("You lose!!")

elif(player == "paper" and computer == "scissors"):
    print("You lose!!")



else:
    print("Something went wrong!! Try again.")