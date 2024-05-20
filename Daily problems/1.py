# Input a year and find whether it is a leap year or not.

# How it works:
# User Input: The program starts by asking the user to enter a year.
# Function is_leap_year: This function takes the year as an argument and checks:
# If the year is divisible by 4.
# If it is divisible by 100 (which makes it not a leap year unless the next condition is met).
# If it is divisible by 400 (which then makes it a leap year despite being divisible by 100).
# Print Result: Based on the return value of the is_leap_year function, the program prints whether the year is a leap year or not.

def leap_year(year):
    # check if the year is divisible by 4
    if year % 4 == 0:
        # check if the year is divisible by 100
        if year % 100 == 0:
            # check if the year is divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# input a year from the user
year = int(input("Enter a year: "))

# determine if it is leap year
if leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
