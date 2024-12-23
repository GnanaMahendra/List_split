'''
Give space-separated numbers,Write a program to print list containing the given numbers.

example:
input:
    10 20 30 40 50
output:
    [10, 20, 30, 40, 50]
'''

number = input()
nums = number.split() #remove the space in the number ver
 
list_output = []

for i in nums:
    num = int(i)
    list_output += [num]
print(list_output)