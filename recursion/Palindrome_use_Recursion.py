def is_palindrome(string):
    # Base case: If the string is empty or has one character, it's a palindrome
    if len(string) <= 1:
        return True
    # Check if the first and last characters are the same
    if string[0] == string[-1]:
        # Recursive case: Check the substring excluding the first and last characters
        return is_palindrome(string[1:-1])
    else:
        return False

# Input string
string = input("Enter a string: ").lower()  # Convert to lowercase for case-insensitive comparison

# Call the is_palindrome function
is_true = is_palindrome(string)

# Print the result
print(is_true)
