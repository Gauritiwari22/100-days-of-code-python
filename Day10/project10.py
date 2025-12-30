# Project 10

print("Welcome to the Python Calculator!")
print("\n")
print("""
 ______________________
|  _________________   |
| |   CALCULATOR    |  |
| |_________________|  |
|  ___ ___ ___   ___   |
| | 7 | 8 | 9 | | + |  |
| |___|___|___| |___|  |
| | 4 | 5 | 6 | | - |  |
| |___|___|___| |___|  |
| | 1 | 2 | 3 | | * |  |
| |___|___|___| |___|  |
| | 0 | . | = | | / |  |
| |___|___|___| |___|  |
|______________________|
""")
print("\n")


condition1=True
condition2=True
while condition1:
    if condition2:

        first_num=int(input("Enter the first number= "))

    operators=["+","-","*","/"]
    for i in operators:
        print(i)
    choice=input("Pick an operation: ")
    second_num=int(input("Enter the second number= "))

    if choice == "+":
        result = first_num + second_num
    elif choice == "-":
        result = first_num - second_num
    elif choice == "*":
        result = first_num * second_num
    elif choice == "/":
        result = first_num / second_num

    print(f"{first_num} {choice} {second_num} = {result}")

    restart=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation or type 'exit' to end: ")
    
    if restart=="y":
        first_num=result
        condition2=False
    elif restart=="n":
        condition2=True
    elif restart=="exit":
        break

print("End of Calculation.")

# Calculator 2 (using the return statement)


print("Welcome to the Python Calculator!")

def calculate(first_num, second_num, operator):
    if operator == "+":
        return first_num + second_num
    elif operator == "-":
        return first_num - second_num
    elif operator == "*":
        return first_num * second_num
    elif operator == "/":
        return first_num / second_num


condition1 = True
condition2 = True

while condition1:

    if condition2:
        first_num = int(input("Enter the first number = "))

    operators = ["+", "-", "*", "/"]
    for op in operators:
        print(op)

    choice = input("Pick an operation: ")
    second_num = int(input("Enter the second number = "))

    result = calculate(first_num, second_num, choice)

    print(f"{first_num} {choice} {second_num} = {result}")

    restart = input(f"Type 'y' to continue with {result}, 'n' for new calculation, or 'exit' to end: ")

    if restart == "y":
        first_num = result
        condition2 = False
    elif restart == "n":
        condition2 = True
    elif restart == "exit":
        break

print("End of Calculation.")


        
    


