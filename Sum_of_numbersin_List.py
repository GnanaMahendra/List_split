'''
A functions os given in the prefilled code that takes a list L as an argument.

Write a program that returns the sum of the numbers in the list L using Recursion.

Example :
Input :
    1 2 4 4
Output :
    11

'''
#Source Code:

def get_sum(number):
    
    if not number:
        return 0
    else:
        return int(number[0]) + get_sum(number[1:])



number = input().split()

print(get_sum(number))