# Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.

# Explanation: User Inputs: The program prompts the user to enter the principal amount, time in years, and rate of
# interest as percentages. These inputs are expected to be numeric, so they are converted to floats. Error Handling:
# The try-except block is used to handle cases where the user enters non-numeric values, catching ValueError and
# notifying the user of the error. Simple Interest Calculation: Simple interest is calculated using the formula (
# P×T×R)/100. This formula computes the interest based on the principal, the time the money is lent for, and the rate
# of interest. Output: The calculated simple interest is displayed to the user using formatted output,
# ensuring clarity and precision.

def main():
    # take input from the user
    try:
        p = float(input("Enter the princple amount (P): "))
        t = float(input("Enter the time period in years (T): "))
        r = float(input("Enter the rate of interest per annum (R) in percentage: "))
    except ValueError:
        print("Invalid input. please enter numeric values.")
        return

    simple_interest = (p * t * r) / 100

    print(f"The simple interest for the given principle, time, and rate is {simple_interest}. ")


main()


# def interestcalculator():
#     c = 'y'
#     while c == 'y':
#         choice = input("Enter 1 to find Simple Interest\nEnter 2 to find Compound Interest \n : ").upper()
#         print()
#         if choice == '1':
#             simpleinterest()
#
#         elif choice == '2':
#             compoundinterest()
#
#         else:
#             print("Invalid Input")
#             exit()
#     else:
#         print('wrong input')
#
#
# def simpleinterest():
#     p = int(input("Enter Principle : "))
#     r = int(input("Enter Rate of Interest : "))
#     t = int(input("Enter Time Period : "))
#     print("Simple Interest = ", p * r * t / 100)
#     ad1 = input("Do you want to run the code again( ENTER Y IF YES ) : ").lower()
#     if ad1 == "y":
#         interestcalculator()
#     else:
#         exit()
#
#
# def compoundinterest():
#     p = int(input("Enter Principle : "))
#     r = int(input("Enter Rate of Interest : "))
#     t = int(input("Enter Time Period : "))
#     print("Compound Interest = ", (p + p * r / 100) ** t)
#     ad2 = input("Do you want to run the code again( ENTER Y IF YES ) : ").lower()
#     if ad2 == "y":
#         interestcalculator()
#     else:
#         exit()
#
#
# interestcalculator()
