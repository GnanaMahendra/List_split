'''
For this problem, the prefilled code will contain a set. 
Write a program to check the following relations with the given set.
    1. Superset
    2. Subset
    3. Disjoint set

Example : 

Input :
    2 3 4
Output :
    Superset
Input :
1 2 3 4 5 6 7 8 9 10 11
Output :
    Subset
Input :
    10 11
Output :
    Disjoint Set

'''


num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Write your code here
num = input().split()

new_set = set ()
for i in num:
    new_set.add(int(i))

if num_set.issubset(new_set):
    print("Subset")
    
elif num_set.issuperset(new_set):
    print("Superset")
elif new_set.isdisjoint(num_set):
    print("Disjoint Set")
    
