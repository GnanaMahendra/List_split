'''
Write a program to remove the elements other ten numbers in the list.

Example :

Input :1,3,@,#,2,.,4,5
Output :[1, 2, 3, 4, 5]

Input :
1,sddf,3,5,7,1,r

Output :
[1, 1, 3, 5, 7]
'''

num = input().split(",")

new_list = []

for i in num:
    if i.isdigit():
        new_list.append(int(i))
print(sorted(new_list))