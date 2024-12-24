'''
For this problem, the prefilled code will contain a function. Write a program that the given function will return the perimeter of the square.
The sum of lengths of the four sides of a square is the perimeter of the square

Sample (I/O)

Input :
    3
Output :
    12
Sample(I/O)

Input :
    5
Output :
    20

'''

#source Code

def perimeter_of_square(arg_1):
    # Write your code here
    return (4*arg_1)
side = int(input())
result = perimeter_of_square(side)
print(result)
