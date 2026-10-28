    program 1
    firstName= input("enter a firstname:")
    lastName= input ("enter a lastname:")
    tonyAge=78
    tonyHeight=1.89
    print ("firstName: "+firstName,"lastName: "+lastName,"Age: ", tonyAge,"Height:" ,tonyHeight)


    program 2
    numberOfPlus = int(input("enter the number of plus signs to display a: "))
    numberOfPlus1 = int(input("enter the number of plus signs to display b: "))
    a=10
    b=90
    def sum(a, b):
        if a==10 and b==90:
            return a + b
        else :
            return "error"
        
    print(sum(numberOfPlus, numberOfPlus1))

    program 3
    votingAge = int(input("enter the voting age: "))

    if votingAge >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

    program 4
    cal1 = int(input("enter the first number: "))
    cal2 = int(input("enter the second number: "))

    print("user enter for there own choice +_-/*/: ")
    operation = input("enter the operation: ")
    def calculate(a, b, operation):
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            if b != 0:
                return a / b
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Invalid operation"
        
        
    print(calculate(cal1, cal2, operation)) 

    program 5

    for i in range(1,101):
        if i % 2 == 0:
            print(i)

    program 6

    studentMarks = [85, 92, 78, 96, 88]
    studentMarks.append(90)
    print(studentMarks)
    highest = 0
    for mark in studentMarks:
        if mark > highest:
            highest = mark
    totalSum=sum(studentMarks)

    average = totalSum / len(studentMarks)

    print("The highest mark is:", highest)
    print("The average mark is:", float(average))

    program 7
    import random

    randomNumber = random.randint(1, 100)
    attempt = 0

    print("Welcome to the game")
    print("choice: 1-100")

    while True:
        try:
            userGuess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempt += 1

        if userGuess < randomNumber:
            print("Too low! Try again.")
        elif userGuess > randomNumber:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempt} attempts.")
            break


    new lecture of python series

    print("enter the number please : ")
    num = int(input())
    def check_number(num):

        if (num%2 == 0):
           return "Even"
        elif (num%2 != 0):
            return "Odd"
        else:
           return "code find un error"
    print(check_number(num))


    cities = ["New York", "London", "Tokyo", "Paris"]
    hero = ["Spider-Man", "Batman", "Superman", "Wonder Woman"]

    def print_length(lst):
        print(len(lst))


    print_length(cities)
    print_length(hero)

    def fun_factorial(n):
        if n == 0:
            return 1``
        else:
            return n * fun_factorial(n-1)
    print(fun_factorial(4)) 

def fun_convert_to_usd(ind_ruppee):
    p=ind_ruppee * 95.61
    return p
print(fun_convert_to_usd(12))

def fun_ind(list, ind=0):
    if ind == len(list):
        return 0
    print(list[ind])
    fun_ind(list, ind+1)

fruits = ["apple", "banana", "orange"]
fun_ind(fruits)
    