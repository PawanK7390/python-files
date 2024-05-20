# Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all.

# Explanation: Loop Until 'x' is Entered: The program uses a while True: loop, which will continue indefinitely until
# explicitly broken out of. This allows the user to continue entering inputs until they decide to stop by entering
# 'x'. User Input: Inside the loop, input() is called to take input from the user. This can be a number or 'x' to
# terminate input. Check for Termination Signal: If the input is 'x', the program breaks out of the loop. Convert
# Input to Number: If the input is not 'x', the program attempts to convert the input into a float. If this
# conversion fails (the input is not a number), a ValueError is caught and an error message is printed, but the loop
# continues. Sum Calculation: If the input is a valid number, it is added to the cumulative sum sum_of_numbers. Print
# the Result: After the loop exits, the program prints the total of all valid numbers entered by the user.

def main():
    sum_of_numbers = 0
    while True:
        user_input = input("Enter a number or 'x' to stop: ")
        if user_input.lower() == 'x':
            break
        try:
            number = float(user_input)
            sum_of_numbers += number
        except ValueError:
            print("invalid input, please enter a valid number or 'x' to exit. ")
        
    print(f"the sum of all entered number is: {sum_of_numbers}")


main()
