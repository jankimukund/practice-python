import re
HISTORY_FILE = "history.txt"

def history_file():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("no history yet")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("history cleared")

def save_to_file(expression, result):
    file = open(HISTORY_FILE, "a")
    file.write(expression + "=" + str(result) + "\n")
    file.close()

def standard_calculator(user):
    parts = re.split(r'\s*([\+\-\*\/])\s*', user.strip())
    
    

    if len(parts) != 3:
        print("Invalid input format. Use: 39+89 or 39 + 89")
        return

    try:
        num1 = float(parts[0])
        op   = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid input! Enter numbers only")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("can't divide by zero!")
            return
        else:
            result = num1 / num2
    else:
        print("Invalid operator! Use +, -, *, or /")
        return

    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_to_file(user, result)


# --- MAIN LOOP ---
print("=== Calculator ===")
print("Commands: 'history', 'clear', 'quit'")
print("Format:   39+89  or  39 + 89\n")

while True:
    user_want = input("Enter calculation: ").strip().lower()
    if user_want == "history":
        history_file()
    elif user_want == "clear":
        clear_history()
    elif user_want == "quit":
        print("Thanks for using calculator")
        break
    elif user_want == "":
        continue
    else:
        standard_calculator(user_want)
