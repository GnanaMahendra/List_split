'''
For this problem , The prefilled code will contain a list of tuples. 
Write a program to replace the last number of each tuple in the list with the given number(n)

Example :
prefilled list 
    
    num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]

Input : 
    50
Output :
    [(10, 20, 50), (1, 50), (5, 10, 15, 50)]
Input :
    -1
Output :
    [(10, 20, -1), (1, -1), (5, 10, 15, -1)]
'''
num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]

num = int(input())
changed_list = []
for i in num_list:

    new_list = list(i)
    new_list.pop()
    new_list.append(num)
    new_list = tuple(new_list)
    changed_list.append(new_list)
print(changed_list)