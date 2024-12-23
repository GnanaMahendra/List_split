'''
Given space-separated number, write a program to print the Smallest number among the given number.

sample (i/o)

input:
    54 10 15 24 7 12
output:
    7
sample (i/o)

input:
    55 6 946 789 38
output:
    6

'''

num = input()

number = num.split()

smallest = 999999999999999999

for i in number:
    a = int(i)
    if a < smallest:
        smallest = a
print(smallest)