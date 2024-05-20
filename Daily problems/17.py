# Subtract the Product and Sum of Digits of an Integer

# Convert the integer to a string to easily iterate over each digit.
# Initialize variables to keep track of the product and sum of the digits.
# Iterate through each digit, converting it back to an integer, and update the product and sum accordingly.
# After iterating through all digits, calculate the difference between the product and the sum.
# Return or print the result.

def sub_product_and_sum(n):
    # Convert integer to string to iterate over digits
    str_n = str(n)

    # Initialize the product and sum
    product = 1
    sum = 0

    # Iterate over each character in the string representation of n
    for i in str_n:
        digit = int(i)
        product = product * digit
        sum = sum + digit

    # Calculate the result by subtracting the sum from the product
    result = product - sum

    # Return result, product, and sum as a tuple
    return result, product, sum


n = int(input("Enter an integer: "))
result, product, sum_digits = sub_product_and_sum(n)
print(f"For the integer {n}:")
print(f"Product of digits: {product}")
print(f"Sum of digits: {sum_digits}")
print(f"Result (Product - Sum): {result}")

# The function now returns a tuple (result, product, sum_digits). This tuple contains three values: the calculated
# result of subtracting the sum from the product, the product of the digits, and the sum of the digits. When calling
# the function, we unpack the returned tuple into three variables: result, product, and sum_digits. This allows for
# individual access to each value for further use or display. Additional print statements are added to display the
# product of the digits, the sum of the digits, and the result separately, providing a clear and detailed output to
# the user.
