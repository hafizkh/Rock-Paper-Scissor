print("--------------------")
print("Rock Paper Scissor")
print("--------------------")

def rock_paper_scissor(user, computer):

    if user == "rock" and computer == "paper":
        print("--------------")
        return "Computer Won"
    elif user == "paper" and computer == "scissor":
        print("--------------")
        return "Computer Won"
    elif user == "scissor" and computer == "rock":
        print("--------------")
        return "Computer Won"
    elif user == computer:
        print("--------------")
        return "Reuslt is Draw"
    else:
        print("--------------")
        return "User Won"