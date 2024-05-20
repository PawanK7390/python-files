# To calculate Fibonacci Series up to n numbers.

# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
# usually starting with 0 and 1.

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    n = int(input("Enter the number to get the fibonacci numbers: "))

    for i in range(n):
        print(fib(i), end=' ')


main()

# While this recursive approach is elegant and a straightforward implementation of the mathematical definition,
# it's not efficient for large values of n. This is because it computes the values of many Fibonacci numbers multiple
# times. For example, fibonacci(4) is calculated as part of fibonacci(5), fibonacci(6), etc.

# Time Complexity
# The time complexity of this recursive approach is O(2^n), which is exponential and grows rapidly as n increases.

