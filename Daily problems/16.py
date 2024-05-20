# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
#
# n = int(input("Enter the number of Fibonacci numbers to generate: "))
#
# for i in range(n):
#     print(fib(i), end=' ')

def fibonacci_memo(n, memo={}):
    # Defines a function named fibonacci_memo that takes two arguments: n (the n-th Fibonacci number to compute) and
    # memo (a dictionary used to store previously computed Fibonacci numbers). memo={} initializes memo as an empty
    # dictionary by default if no argument is passed, acting as the memoization cache.

    if n in memo:
        return memo[n]
    # This line checks if the Fibonacci number for n has already been computed and stored in the memo dictionary. If
    # n is found in memo, it returns the stored result, avoiding redundant calculations.

    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    # If n is not in the memo and is greater than 1, the function computes it by recursively calling itself to obtain
    # F(n-1) and F(n-2), the two preceding Fibonacci numbers. Storing Computed Value: Once the value for F(n) is
    # computed, it's stored in the memo dictionary with n as the key. This storage step is crucial as it saves the
    # result for future reference, which is the essence of memoization. Return the Result: Finally, it returns the
    # computed Fibonacci number for n.
    else:
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        return memo[n]


# Example usage to print series
n = int(input("Enter the number of Fibonacci numbers to generate: "))
for i in range(1, n+1):
    print(fibonacci_memo(i), end=' ')
