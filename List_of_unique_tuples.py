'''
Write a program to print lists which contain the unique element in the given list of lists.

Sample I/O
Input :
Enter the no of the list : 3
Enter the list elements :1 2 3 3
Enter the list elements :4 5 6 7 1
Enter the list elements :1 2 3 4 4

Output :
[[4, 5, 6, 7, 1]]

Input :
Enter the no of the list : 3
Enter the list elements :1 2 3 4 5 5
Enter the list elements :1 2 3 4 5 6
Enter the list elements :0 9 8 7 6 4
Output :

Unique lists : [[1, 2, 3, 4, 5, 6], [0, 9, 8, 7, 6, 4]]
'''

def convert_int_list (num):
    newlist = []
    for i in num:
        newlist.append(int(i))
    return newlist

n = int(input("Enter the no of the list : "))

result_list = []

for i in range(n):
    num = input("Enter the list elements :").split()
    converted_list = convert_int_list(num)
    new_set_list = set(converted_list)
    if len(num) == len(new_set_list):
        result_list.append(converted_list)
msg = "Unique lists : {}"
print(msg.format(result_list))
