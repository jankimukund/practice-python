import random
playing =True
while playing:

    choice = input("roll the dice(y/n): ").lower()

    if choice == 'y':
        dais1=random.randint(1,6)
        dais2=random.randint(2,6)
        print(f'({dais1},{dais2})')
    elif choice=="n":
        print("thanks for playing")
        break
    else: 
        print("invalid choice")
