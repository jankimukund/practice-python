import random

number_to_guess_number = random.randint(1,100)
while True:

    try:
        user_input=int(input ("guess the number between 1 to 100:  "))
        if user_input <number_to_guess_number:
            print("too low")
        elif user_input >number_to_guess_number:  
            print("too high")
        else:
            print("congress! your get correct number") 
        continue       
    except ValueError:
        print( "Please enter a valid number")



