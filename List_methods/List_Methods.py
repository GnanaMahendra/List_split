'''
Consider a list (num_list = []). Write a program to perform the following commands on the list
    1. insert I E - insert the integer E at index I
    2. append E - insert integer E at the end of the list
    3. pop - remove the list element
    4. reover E - remove the first occurrence of integer E
    5. sort - sort the list in ascending order
    6. print - print the list

Example :

Input :
    5
    append 5
    insert 0 2
    append 1
    sort
    print
Output :
    [1, 2, 5]
Input :
    7
    print
    append 8
    append 7
    insert 2 1
    remove 8
    pop
    print
Output :
    []
    [7]
    
'''
n = int(input())

list_n = []

for i in range(n):
    comand = input().split()
    if comand[0] == "append":
        list_n.append(int(comand[1]))
    elif comand[0] == "insert":
        list_n.insert(int(comand[1]), int(comand[2]))
    elif comand[0] == "sort":
        list_n.sort()
    elif comand[0] == "pop":
        list_n.pop()
    elif comand [0] == "remove":
        list_n.remove(int(comand[1]))
    elif comand[0] == "print":
        print(list_n)
