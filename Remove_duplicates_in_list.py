'''
Write a program to remove duplicate numbers in the list.

Example : 

Input :
    10 10 30 20 40 50 50 30 50 60 70 10
Output :
    [10, 20, 30, 40, 50, 60, 70]
Input :
    20 40 90 20 40 10 50 40 60 80 -1 -2 -3 -2 4 0
Output :
    [-3, -2, -1, 0, 4, 10, 20, 40, 50, 60, 80, 90]
'''

num = input().split()
num_set = set()

for i in num:
    num_set.add(int(i))

num_list = sorted(list(num_set))
print(num_list)