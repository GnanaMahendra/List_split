'''
Given space-separated numbers, Write a program to print a list containing the given number that are divisible by 3.

sample (i/o)1

input:
    3 10 9 11 18 20
output:
    [3, 9, 18]
sample (i/o)2

input:
    300 485 142 1596
output:
    [300, 1596]

'''

num = input()

number = num.split()

list_out =[]

for i in number:
    a = int(i)
    if (a %3 == 0):
        list_out += [a]
print(list_out)