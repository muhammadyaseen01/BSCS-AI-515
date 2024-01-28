# Task 1: Introduction
print("Welcome to the Basic Calculator Program!")

# Task 2: Terminal
print("\nTask 2: Terminal - Open your terminal to run this program.")

# Task 3: Python Interpreter
print("\nTask 3: Python Interpreter - Install Python on your system.")

# Task 4: Variables
print("\nInitializing a variable to store the result")
result = 0  

# Task 5: Text Editor
print("\nTask 5: Text Editor - Use any Text Editor to write python code and use extention'.py' to run.")

# Task 6: Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Task 7: Lists and Tuples
operations = ['Addition', 'Subtraction', 'Multiplication', 'Division']
# operations = ('Addition', 'Subtraction', 'Multiplication', 'Division')

# Task 9: The For Loop
print("\nTask 9: For Loop - Please choose an operation:")

for i in range(len(operations)):
    # print(str(i + 1) + ". " + operations[i])
    print((i + 1),": ",operations[i])



# Task 8: Conditional Statements
# Task 10: User Input and the While Loop
choice = int(input("Enter the number corresponding to your choice: "))


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

while True:
    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)
    else:
        print("Invalid choice, Please choose a number between 1 and 4")
        break

    print("\nResult of",operations[choice - 1],"is:",result)
    break
