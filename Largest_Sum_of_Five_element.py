'''
Given comma-separated numbers, Write a program to print the maximum possible sum with 5 numbers of the given Comma-separated numbers.

Sample (I/O)
Input :
    12, 1, 22, 6, 14,7
Output :
    61
Sample (I/O)
Input :
    70, 43,3,89,65,27,64,75
Output :
    365
'''
#Source Code :

num = input("Enter the Numbers : ")
num = num.split(",")

list_num = []

for i in num:
    list_num += [int(i)]

sorted_list = sorted(list_num , reverse = True)

print(sum ( sorted_list [:5] ))
