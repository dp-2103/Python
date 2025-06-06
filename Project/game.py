import random

choice = ['rock', 'paper', 'scissor']

user_score = 0
computer_score = 0

while True:

    print("select rock, paper or scissor")

    user = input("Enter your choice: ").lower()

    if user not in choice:
        print("Invalid choice!, try again")
        continue

    else:
        computer = random.choice(choice)
        print("computer's choice: ", computer)

        if computer == user:
            print("it's  draw")

        elif (computer == 'rock' and user == 'paper') or\
             (computer == 'paper' and user == 'scissor') or\
             (computer == 'scissor' and user == 'rock'):
                print("you win!")

                user_score += 1

        else:
            print("you lose")
            computer_score += 1
    
    print(f"Score => You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")

#ask to play again
    again = input("Press y/n to play again: ")

    if again != "y":
        print("game ended")
        print(f"Final score ==> you: {user_score}  |  computer: {computer_score} " )
        break
