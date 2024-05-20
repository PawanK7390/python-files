# Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)

def main():
    operation = input("Choose the operator to perform the operation on the inputted numbers (+, -, *, /): ")
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    if operation == '+':
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}.")
    elif operation == '-':
        result = num1 - num2
        print(f"The difference between {num1} and {num2} is {result}.")
    elif operation == '*':
        result = num1 * num2
        print(f"The product of {num1} and {num2} is {result}.")
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The quotient of {num1} and {num2} is {result}.")
    else:
        print("Invalid input. Please choose a valid operator.")

main()
