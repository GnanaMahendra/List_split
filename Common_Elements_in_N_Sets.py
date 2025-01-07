'''
Write a program to find the common elements in the N sets.

Example :

Input :
3
2 1 3 10
21 1 10 44
44 55 10 1
Output :
[1, 10]

Input :
    4
    11 22 33 44 55 66
    11 12 14 33 66 10
    88 11 00 44 33
    1 11 0 5 33
Output :

    [11, 33]

<<<<<<< HEAD
Input :
4
2 4 6 8 10 12
2 4 8 12 16 10
2 5 10 12 15 20 4
12 10 4 8

Output :
[4, 10, 12]

'''
def interSection_of_lists(new_list_alla):
    result= new_list_alla[0]
    for i in (new_list_alla):
        result = result.intersection(i)
=======
'''
def interSection_of_lists(new_list_alla):
    list_1 = new_list_alla[0]
    for i in range(1, len(new_list_alla)):
        list_2 = new_list_alla[i]
        result = (list_1 & list_2)
>>>>>>> master
    return result


    
def convert_list(num):
    new_list = []
    for i in num:
        new_list.append(int(i))
    return new_list

n = int(input())
new_list_alla = []
for i in range(n):
    num = input().split()
    int_num = convert_list(num)
    int_num = set(int_num)
    new_list_alla.append(int_num)

result = interSection_of_lists(new_list_alla)
result = sorted(list(result))
print(result)