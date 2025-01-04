'''
Given lists A and B of space-separated elements, each on a new line of the same length. Write a program to insert the elements of list B into list A at odd indices.

Example :
Input :
    Enter the List- A : Gnana sai 
    Enter the List- B : Mahendra varma
Output :
    ['Gnana', 'Mahendra', 'sai', 'varma']

 
'''
list_A = input("Enter the List- A : ").split()
list_B = input("Enter the List- B : ").split()

increment = 1 

for i in list_B:
    list_A.insert(increment,i)
    increment +=2
print(list_A)