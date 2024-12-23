'''
Given a list of numbers, Write a program to print the sum of the numbers in the list.

sample (i/o)

input1:
    2 5 10 -15 3
output:2 5 10 -15 3
    5
input2:
    -50 20 3 88 17 3 11 200 1800
output:
    2092
'''

num = input()
number = num.split()

sum = 0

for i in number:
    a = int(i)
    sum += a
print(sum)