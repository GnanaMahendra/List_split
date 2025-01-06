'''
Given two lines of comma-separated integers,
Write a program print the numbers that are present in both of the lines.


Example :

Input :
    Enter the First line numbers :  1,-1,3,66,7,3,2
    Enter the second line numbers :  1,3,-3,2,-1,2,-1
Output : 
    [-1, 1, 2, 3]
    
'''
def convert_list_num (num):
    set_num = set ()
    for i in num:
        set_num.add(int(i))
    return set_num


num_1 = input("Enter the First line numbers :  ").split(",")
num_2 = input("Enter the second line numbers :  ").split(",")

num_1 = convert_list_num(num_1)
num_2 = convert_list_num(num_2)

result = sorted (list (num_1 & num_2))

print(result)
