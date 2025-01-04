'''
Give space-separated numbers, Write a program to find even number and odd numbers in one list sorted in ascending order and print odd numbers in another list sorted in ascending order.

Example :
Input :
    3 8 5 7 1 6
Output :
    [6, 8]
    [1, 3, 5, 7]
Input :
    15 20 32 45 66 78 99
Output :
    [20, 32, 66, 78]
    [15, 45, 99]
'''

num = input("Enter the numbers : ").split()

evne_num = []
odd_num = []

for i in num:
    if int(i) % 2 == 0:
        evne_num.append(int(i))
    elif int(i) % 2 != 0:
        odd_num.append(int(i))

even = sorted(evne_num)
odd = sorted(odd_num)
print(even)
print(odd)