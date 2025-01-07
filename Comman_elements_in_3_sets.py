'''
write a program to find the common elements in the three sets.

Example 

Input :
    2 4 6 8 10
    4 8 10 12 16 
    5 10 15 30

Output :
    [10]
Input :
    1 3 5 6 7 8 9
    2 4 6 8 9
    12 6 8 9 33 4

Output :
    [6, 8, 9]
'''
def convert_int_list(num):
    new_set = set()
    for i in num:
        new_set.add(int(i))
    return new_set


num_1 = input().split()
num_2 = input().split()
num_3 = input().split()

num_1 = convert_int_list (num_1)
num_2 = convert_int_list (num_2)
num_3 = convert_int_list (num_3)

intersection_sets = ((num_1 & num_3) & (num_2 & num_3))

result_list = sorted(list(intersection_sets))

print(result_list)