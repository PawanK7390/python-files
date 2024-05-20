# Factorial Program

# def factorial(n):
#     if n == 0:
#         return 1
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
#
# n = int(input("Enter a non-negative integer: "))
# print(f"The factorial of {n} is: {factorial(n)}")

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)


n = int(input("Enter a non-negative integer: "))
print(f"The factorial of {n} is: {factorial_recursive(n)}")
