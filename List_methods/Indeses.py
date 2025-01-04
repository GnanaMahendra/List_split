'''
Write a program that reads a number N and print the index of the given number n in the list l. if there are multiple occurrences of n , print all indices separated by a space.

Exapmle :
Input :
    10
Output : 
    2
Input :
    4
Output : 
    1 8 9
'''

list_a = [5, 4, 10, 2, 3, 2, 5, 15, 4, 4]
# write your code here
num = int(input())
ind = []
for i in range(len(list_a)):
    if list_a[i] == num:
        ind .append(str(i))

print(" ".join((ind)))