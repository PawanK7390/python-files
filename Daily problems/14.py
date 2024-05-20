# To find Armstrong Number between two given number.

# program that iterates through each number in the specified range, checks whether each number is an Armstrong
# number, and then prints it if it is. An Armstrong number (also known as a narcissistic number) is a number that is
# equal to the sum of its own digits each raised to the power of the number of digits.

def is_armstrong(number):
    # convert number to sting to facilitate iteration over digits
    str_num = str(number)
    # calculate the number of digits
    num_digits = len(str_num)
    # calculate the sum of digits raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in str_num)
    # check if the sum of the powers is equal to the original number
    return sum_of_powers == number


def find_armstrong(start, end):
    # iterate over the range from start to end
    for num in range(start, end + 1):
        if is_armstrong(num):
            print(num, "Is an armstrong number. ")


# Input start and end values from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Find and print all Armstrong numbers in the range
find_armstrong(start, end)

# Explanation:
# is_armstrong function:
# Converts the number into a string to easily iterate over each digit. Determines the number of digits (num_digits).
# Computes the sum of each digit raised to the power of the total number of digits (sum_of_powers). Checks if the sum
# of these powered digits equals the original number, returning True if it is an Armstrong number and False otherwise.
# find_armstrong_numbers function:
# Iterates through each number in the given range (from start to end).
# Uses the is_armstrong function to check if the current number is an Armstrong number.
# Prints the number if it is an Armstrong number.
