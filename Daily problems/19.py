# Take integer inputs till the user enters 0 and print the sum of all numbers

def sum_until_zero():
    total_sum = 0
    while True:  # Create an infinite loop
        num = int(input("Enter a number (enter 0 to stop): "))
        if num == 0:
            break  # Exit the loop if the number is 0
        total_sum += num  # Add the number to the total sum

    print(f"The sum of all entered numbers is: {total_sum}")


# Call the function to start taking inputs and calculating the sum
sum_until_zero()
