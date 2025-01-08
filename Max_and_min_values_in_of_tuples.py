'''
Write a program to print the maximum and minimum of all the values at index zero and index one in the list of tuples.

Sample I/O

Input :
3
1 5
3 2
5 8
Output :
(5, 1)
(8, 2)

Input :
4
1 2
2 5
10 1
-3 6
Output :
(10, -3)
(6, 1)
'''

n = int(input())

zero_index_list =[]
one_index_list = []

for i in range(n):
    num = input().split()
    zero_ele = int(num[0])
    zero_index_list.append(zero_ele)
    one_ele = int(num[1])
    one_index_list.append(one_ele)

print((max(zero_index_list),min(zero_index_list)))
print((max(one_index_list) , min(one_index_list)))