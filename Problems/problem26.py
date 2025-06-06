'''
The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score

# here i am using my rock paper scissor  game and the score of that game will be saved in another text file.
'''

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
    

    #ask to play again
    again = input("Press [y/n] to play again: ")

    if again != "y":
        print("\nGame Ended")
        print(f"Final score ==> you: {user_score}  |  computer: {computer_score} " )
        
        #store the final score to score.txt
        with open("score.txt", "a") as f:
            f.write(f"score : {user_score} \n")

        break
        
        
