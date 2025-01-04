'''
Write a program to remove all the occurrences of the given number in a list.

Example :
Input :
    5
Output :
    [10, 20, 35, 50, 20, 100, 200, 10, 150, 100, 100]
'''
nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100]
# Write your code here
num = int(input())
count = nums_list.count(num)
for i in range(count):
    nums_list.remove(num)
print(nums_list)