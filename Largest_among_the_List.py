'''
you are given space-separated integers as input. write a program to print the maximum number among the given numbers.

sample (i/o)

input:
    1 2 3 4 6 9
output:
    9
'''
num = input().split()
len_of_list = len(num)
largest_num = num[0]
for i in num :
    if int(i) > int(largest_num):
        largest_num = int(i)
print(largest_num)