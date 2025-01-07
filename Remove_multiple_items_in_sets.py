'''
For this problem, the prefilled code will contain a set.
Write a program to remove a list of numbers if present in the set.

Example :
In Prefilled set :
num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

Input :
    20 40 80
Output : 
    [10, 30, 50, 60, 70, 90, 100]

Input :
    10 90
Output :
    [20, 30, 40, 50, 60, 70, 80, 100]
'''
num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

num = input().split()
num_list = []
for i in num:
    num_list.append(int(i))

result = num_set.difference(num_list)

result = sorted(list(result))

print(result)