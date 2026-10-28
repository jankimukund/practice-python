

import random

while True:
    computer=random.choice(["R","P","S"])
    user_choice=input("enter your choice(R/P/S): ").upper()
    if user_choice in ["R","P","S"]:
        print(f"computer choice: {computer}")
        if user_choice==computer:
            print("tie")
        elif user_choice == "R" and computer == "S":
            print("You Win! Rock beats Scissors")
        elif user_choice == "R" and computer == "P":
            print("You Lose! Paper beats Rock")
        elif user_choice == "P" and computer == "R":
            print("You Win! Paper beats Rock")
        elif user_choice == "P" and computer == "S":
            print("You Lose! Scissors beats Paper")
        elif user_choice == "S" and computer == "P":
            print("You Win! Scissors beats Paper")
        elif user_choice == "S" and computer == "R":
            print("You Lose! Rock beats Scissors")
    else: 
        print("Invalid choice! Enter R, P or S only") 
        continue
    while True:       
        play_again=input("do you want too play again (y/n): ").lower()
        if play_again == "y":
            break
        elif play_again == "n":
            print("thanks for playing")
            exit()
        else:
            print("Invalid choice! Enter y or n only")
        
