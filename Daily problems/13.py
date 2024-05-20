# To find out whether the given String is Palindrome or not.

def is_palindrome(s):
    # Normalize the string: lower case and remove non-alphanumeric characters
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())

    # Initialize two pointers, one at the start and one at the end of the string
    left = 0
    right = len(s) - 1

    # Compare characters from the start and end moving towards the center
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# Input string from user
input_string = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(input_string):
    print(f"The string '{input_string}' is a palindrome. ")
else:
    print("The string is not a palindrome. ")


# Explanation: Normalization: Converts the string to lower case and filters out non-alphanumeric characters. This
# step ensures the comparison is case-insensitive and not affected by punctuation or spaces. Non-alphanumeric
# characters are removed using ''.join(char for char in s if char.isalnum()). This ensures that punctuation and
# spaces do not affect the palindrome check. Two Pointers: Uses two pointers to compare characters. One pointer
# starts at the beginning (left), and the other at the end (right). This is similar to what you might see in a C++ or
# Java implementation where you often use indexing to compare elements. Character Comparison: The while loop
# continues as long as left < right, checking characters at these positions for equality. If any pair of characters
# does not match, the function returns False, indicating the string is not a palindrome. If the loop completes
# without finding mismatches, it returns True.


# def is_palindrome(s):
#     # Convert to lower case to make the check case-insensitive
#     s = s.lower()
#     # Remove all non-alphanumeric characters
#     s = ''.join(char for char in s if char.isalnum())
#     # Check if the string is equal to its reverse
#     return s == s[::-1]
#
#
# # Input string from user
# input_string = input("Enter a string to check if it's a palindrome: ")
# if is_palindrome(input_string):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")
#
# # Normalize the String: Convert the string to lower case using lower() and remove any non-alphanumeric characters to
# # ensure the palindrome check is consistent regardless of case, spaces, or punctuation. Reverse and Compare: The
# # string is reversed using slicing (s[::-1]) and compared with the original normalized string. Output: The function
# # is_palindrome returns True if the string is a palindrome and False otherwise. Based on the result, a message is
# # printed to indicate whether the input string is a palindrome.
