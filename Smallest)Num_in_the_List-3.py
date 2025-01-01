'''

Given comma-separated numbers and an index write a program to print the Smallest number among the numbers from the given index I to the end of the list.

For example, if the given comma-separated numbers are 1,9,3,1,2,7,4,8 and I = 2

    • The numbers and their respective index values are,

Indices
    • The numbers from index 2 are 3, 1, 2, 7, 4, and 8.
    • The Smallest number from index 2 is 1.

The output should be 1.

'''
#Smallest number based on the index number

def getting_list(num):
    getting_list = []
    for i in num:
        getting_list += [int(i)]
    return getting_list


num = input("Enter the number(1,2,33,45,2) : ").split(",")
index = int(input())
result = getting_list(num)
print("Smallest Number : " + str(min(result[index:])))