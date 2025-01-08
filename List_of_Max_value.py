'''
Write a program to create a list with maximum value in each list.

Sample I/O

Input : 
Enter the no of list entered :  3
1 2 3 4 5 6 
11 22 33 44 55 66
111 222 333 444 555 666

Output :

The 3 no of list this are the maximum numbers : [6, 66, 666]
'''
def convert_list(num):
    new_list = []
    for i in num:
        new_list.append(int(i))
    return new_list

n = int(input("Enter the no of list entered :  "))

result = []
for i in range(n):
    num = input().split()
    list_int = convert_list(num)
    max_val = max(list_int)
    result.append(max_val)

msg = "The {} no of list this are the maximum numbers : {}"

print(msg.format(n, result))
