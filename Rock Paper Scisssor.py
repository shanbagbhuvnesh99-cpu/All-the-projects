# Rock Paper Scissor Game

'''
Rock == 0
Paper == 1
Scissor == 2
'''

import random 

user_choice = int(input("Enter your choice: 0 for Rock, 1 for Paper, and 2 for Scissor\n"))
computer_choice = random.randint(0, 2)

print(f"Computer chose {computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
