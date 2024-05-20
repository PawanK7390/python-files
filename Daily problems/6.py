# Write a program to print whether a number is even or odd, also take input from the user.

def main():
    num = input("Enter a number to check if it is even or odd: ")
    # check if the input is a number
    try:
        number = int(num)    # convert input to integer
    except ValueError:
        print("Invalid input. please enter a valid integer. ")
        return

    # check if the number is even or odd
    if number % 2 == 0:
        print(f"the number {number} is even.")
    else:
        print(f"the number {number} is odd.")


main()
