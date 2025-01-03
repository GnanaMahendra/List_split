def get_largest_square(numbers):
    # Base case: if the list is empty, return 0
    if not numbers:
        return 0
    else:
        # Recursive case: square the first number and compare with the largest square of the rest
        current_square = int(numbers[0]) ** 2
        return max(current_square, get_largest_square(numbers[1:]))

# Input: numbers as a space-separated string
numbers = input("Enter numbers separated by spaces: ").split()

# Call the get_largest_square function
result = get_largest_square(numbers)
print("The largest square is:", result)
