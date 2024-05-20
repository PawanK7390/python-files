# Take integer inputs till the user enters 0 and print the largest number from all.

# def max():
#     max = 0
#     while True:  # Create an infinite loop
#         num = int(input("Enter a number (enter 0 to stop): "))
#         if num == 0:
#             break  # Exit the loop if the number is 0
#         elif max < num:
#             max = num
#     print(f"The max of all entered numbers is: {max}")
#
#
# max()

def find_max_number():
    max_num = None  # Initialize max_num to None to handle any type of number
    while True:
        num = int(input("Enter a number (enter 0 to stop): "))
        if num == 0:
            break
        if max_num is None or num > max_num:
            max_num = num

    if max_num is None:
        print("No numbers were entered.")
    else:
        print(f"The max of all entered numbers is: {max_num}")


# Call the function
find_max_number()

# Initialized max_num to None to correctly handle the case where no numbers are entered or all entered numbers are
# negative. This ensures that any first entered number sets the initial max_num value.

# The if max_num is None or num > max_num: check allows max_num to be updated if it's still None (meaning no previous
# number was greater) or if the current num is greater than the current max_num.

# Added a check to see if max_num remains None after the loop, which indicates that no numbers were entered before
# stopping. This avoids printing an incorrect or misleading message.
