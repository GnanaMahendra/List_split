'''
Find the First element in the list
Write a program that return the index of the first occurrence of the given numbers in the list using recursion.

Example (O/I)
Input : 
    7 1 3 8 4 3 8
    8
Output :
    3
'''

#Find the first Element in the List

def get_index(number_list , number, index = 0 ):
    #base case
    if not number_list:
        return -1
    if int(number_list[0]) == number:
        return index
    else:
        return get_index(number_list[1:] , number , index+1)

number_list = input().split()
number = int(input())


number_index = get_index(number_list , number)
print(number_index)