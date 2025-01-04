'''
Given comma-separated numbers, write a program to find the Mode of the given numbers.

Note

    Mode is the number that occurs more times than other numbers in the list.
    For example, if the given list of numbers are 6, 3, 9, 3, 6, 6, 5, 9, 3,
    The number 6 occurred 3 times.
    The number 3 occurred 3 times.
    The number 9 occurred 2 times.
    The number 5 occurred 1 time.
    The Modes are 6 and 3, as they occurred more times than the other numbers in the given list.
    If there are multiple modes, print the mode that occurs first in the given numbers.
    Among 6 and 3, 6 occurs first in the given numbers.


Input :
    1,5,9,1,4,7,5,3,5,6,8,5
Output :
    5
Input :
    6,3,9,3,6,6,5,9,3
Output :
    6
'''

num = input().split(",")
s = 0
a = ""
for i in num:
    count = num.count(i)
    if count > s:
        s = count
        a = i
print(a)