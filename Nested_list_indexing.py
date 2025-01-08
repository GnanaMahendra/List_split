'''
For this problem, the prefilled code will contain a list of tuples. write a program to print the index of the given  number N in the list of tuples.

Sample input and Output :

Input :

'''

num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]

num  = int(input())

for i in num_list:
    index_1 = num_list.index(i)
    if num in i:
        index_2 = i.index(num)
        msg = "{} {}"
        print(msg.format(index_1,index_2))
        break