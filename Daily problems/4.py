# Take 2 numbers as inputs and find their HCF and LCM.

# Input Numbers: The program begins by asking the user to input two numbers. Compute HCF: The compute_hcf function
# implements the Euclidean algorithm, which repeatedly replaces the larger number by its difference with the smaller
# number until one of the numbers becomes zero. The last non-zero value is the HCF. Compute LCM: The compute_lcm
# function uses the relationship between HCF and LCM: LCM(a,b) = |a X b|/(HCF(a,b)) . This ensures that the LCM is
# calculated based on the previously computed HCF.


# Function to compute the HCF (Greatest Common Divisor) using the Euclidean algorithm
def find_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

# Function to compute LCM using the formula LCM(a, b) = abs(a*b) / HCF(a, b)
def find_lcm(x, y):
    hcf = find_hcf(x, y)
    return abs(x * y) // hcf


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate HCF
hcf = find_hcf(num1, num2)

# Calculate LCM
lcm = find_lcm(num1, num2)

print(f"The HCF (GCD) of {num1} and {num2} is: {hcf}")
print(f"The LCM of {num1} and {num2} is: {lcm}")
