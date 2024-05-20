# Input a number and print all the factors of that number (use loops).

# program that inputs a number and prints all the factors of that number, you can use a loop to check divisibility
# from 1 up to the number itself. A factor of a number n is an integer d that divides n without leaving a
# remainder.

def factors(x):
    print(f"the factors of {x} are: ")
    # # in descending order
    # for i in range(x + 1, 0, -1):
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


num = int(input("Enter a number to find its factors: "))
factors(num)
