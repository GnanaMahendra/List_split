'''
Write a program that rads comma-separated numbers and the numbers K and the find all the unique pairs in the given numbers Whose sum is equal to K.

Example :

Input :
Enter the comma-separated numbers : -4,-3,-2,-1,0,1,2,3,4,5,6
Enter the pairs sum : -1

Output:
(-4, 3)
(-3, 2)
(-2, 1)
(-1, 0)

Input :
Enter the comma-separated numbers : 5,3,7,9,5
Enter the pairs sum : 12
Output :
(3, 9)
(5, 7)
'''

def unique_pairs_list (int_list ,pairs_sum):
    unique_pairs_set = set()

    for i in range(len(int_list)-1):
        num_1 = int_list[i]
        num_2 = pairs_sum - num_1
        if num_2 in int_list[i+1 : ]:
            pair = (num_1, num_2)
            sorted_pair = tuple(sorted(pair))
            unique_pairs_set.add(sorted_pair)
    
    return unique_pairs_set

def convert_int_list(num):
    new_list =[]
    for i in num:
        new_list.append(int(i))
    return new_list


num = input("Enter the comma-separated numbers : ").split(",")
pair_sum = int(input("Enter the pairs sum : "))

int_list = convert_int_list(num)

unique_pairs = unique_pairs_list(int_list,pair_sum)
unique_pairs = list(unique_pairs)
unique_pairs.sort()
for i in unique_pairs:
    print(i)