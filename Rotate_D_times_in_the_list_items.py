'''
Write a program that reads the comma-separated integers and a positive integer D , then rotates the numbers D times to the left , and prints the rotated list.

Exaple :

Input :
    1,2,3,4,5
    3
Output :
    [4, 5, 1, 2, 3]

Input :
Enter the comma-separated numbers : 3,4,5,6,7,1,2,4
Enter the Rotated times in numbers : 88
Output :
    [3, 4, 5, 6, 7, 1, 2, 4]

'''

def convert_int_list(num):

    new_list = []
    for i in num:
        new_list.append(int(i))
    return new_list

num = input("Enter the comma-separated numbers : ").split(",")
rotated_num = int(input("Enter the Rotated times in numbers : "))

int_num = convert_int_list(num)

rotated_times = rotated_num % len(int_num)

first_part = int_num[:rotated_times]
second_part = int_num [rotated_times:]

second_part.extend(first_part)

print(second_part)
