'''
Write a program that returns the sum of the square of the numbers in the list using Recursion.

example:

Input :
    2 3 4
Output :
    29
'''
#Sum of the Square of the given numbers

def sum_squ_of_num(numbers):
    
    if not numbers: # Base case 
        return 0
    else:
        # Recursive case
        return int(numbers[0]) ** 2 + sum_squ_of_num(numbers[1:])

#
numbers = input().split()
print(sum_squ_of_num(numbers)) #passing the arguments