'''
Write a program to find the missing numbers from 1 to maximum numbers in the list.
Example :

Input :
1 2 4 5 6 8 9
Output :
[3, 7]
'''

num = input().split()

new_list = []

for i in num:
    new_list.append(int(i))

num_set = set ()

max_num = max(new_list)

for i in range(1 , max_num+1):
    num_set.add(i)

result = num_set.difference(new_list)

print(sorted(list(result)))