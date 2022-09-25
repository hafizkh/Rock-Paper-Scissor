import rpsUtils
import random

def playGame():
    print("****Welcome to the Rock-Paper-Scissor Game!****")
    while True:

        user = input("Please Choose Rock, Paper, or Scissor: ").lower()
        computer = random.choice(["Rock", "Paper", "Scissor"]).lower()
        print("\n")
        print("User Selected: " , user)
        print("Computer selected: ", computer)
        print("\n")
        print(rpsUtils.rock_paper_scissor(user, computer))
        print("--------------")


playGame()