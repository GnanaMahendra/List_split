'''
Write a program count all the occurrences of the given number n in the list.

Example :
Input :
    5
Output :
    2
'''



nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100, 20, 20]
n = int(input())# Write your code here
count = nums_list.count(n)
print(count)