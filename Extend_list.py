'''
Given a number n , Write a program that reads n lines of input containing spaces-separated string and print a list of all the string on n lines sorted in ascending order.

Example :
Input : 
    3
    1 3 55
    6 mahi
    4 gnana    
Output :
    ['1', '3', '4', '55', '6', 'gnana', 'mahi']
'''

n = int(input())

list_contain = []

for i in range(n):

    num = input().split()

    for i in num:
        
        list_contain.eppend(i)

final_list = sorted (list_contain)

print(final_list)