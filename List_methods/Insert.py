'''
Write a program add the specific location to add the value to the list.

Example :

Input :
    30
    2
Output :
    [10, 20, 30, 40, 40]

50
5
[10, 20, 30, 40, 50, 50]
'''
List_a = [10,20,30,40,50]
num =int(input())
index = int(input())

List_a.insert(index, num)
print(List_a)