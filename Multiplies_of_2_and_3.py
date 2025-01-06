'''
Given an Integer N. 
Write a program to create two sets with N multiples of 2 and 3 and print the following.
    1. All the multiples of 2 but not the multiplies 3.
    2. uncommon multiples of 2 and 3.

Example : 

Input : 
     5
Output :
    [2, 4, 8, 10]
    [2, 3, 4, 8, 9, 10, 12, 15]
Input : 
    8
Output :
    [2, 4, 8, 10, 14, 16]
    [2, 3, 4, 8, 9, 10, 14, 15, 16, 18, 21, 24]
    

'''

num = int(input())

set_2_multi = set ()
set_3_multi = set ()

for i in range(1, num +1):
    set_2_multi.add(i * 2)
    set_3_multi.add(i * 3)

<<<<<<< HEAD
set_deff = set_2_multi - set_3_multi
set_symmentric_deff = set_2_multi ^ set_3_multi

print(sorted(list(set_deff)))
print(sorted(list(set_symmentric_deff)))
=======
dup = list(set_2_multi)

for i in dup:
    if i % 2 == 0 and i % 3 == 0:
        set_2_multi.remove(i)
        set_3_multi.discard(i)

result = sorted(list(set_2_multi | set_3_multi))

print(sorted(list(set_2_multi)))
print(result)
>>>>>>> master
