'''
Given space-separated numbers,
Write a program to print the list of numbers that occur an odd number of times
Print the numbers in a sorted order.

Example :

Input :
    1 2 3 4 4 4 3 2 1 1 1 1
Output :
    [1, 4]

'''
num = input("Enter the space-separated numbers : ").split()

new_list = []

for i in num:
    count = num.count(i)
    if int(i) in new_list:
        continue
    if count % 2 != 0:
        new_list.append(int(i))

print(sorted(new_list))