import random

choices = ["rock", "paper", "scissor"]


print('''select any one from rock, paper, scissor''')

#selectrion of choices
computer = random.choice(choices)
user = input("enter your choice: ").lower()

#print of computer's choice
print("computer's choice: ", computer)

if user not in ["rock", "paper", "scissor"]:
    print("invalid choice! try again")
    continue

if (computer == user):
    print("it's a Draw!")

elif(computer == "rock" and user == "paper"):
    print("you win")
elif(computer == "paper" and user == "scissor"):
    print("you win")
elif(computer == "scissor" and user == "rock"):
    print("you win")

else:
    print("you lose")

print("thank you for playing!")



