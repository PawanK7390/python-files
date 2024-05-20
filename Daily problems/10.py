# Take 2 numbers as input and print the largest number.

def main():
    # Taking two numbers as input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Comparing the two numbers
    if num1 > num2:
        print(f"The largest number is {num1}")
    elif num2 > num1:
        print(f"The largest number is {num2}")
    else:
        print("Both numbers are equal.")


main()
