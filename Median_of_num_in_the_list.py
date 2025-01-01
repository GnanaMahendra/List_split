'''
Given Comma-separated numbers ,Write a program to print the Median of the given number.


Note :
Median is the middle value of the given number, Where the numbers should be is ascending order.
For example, if number are 1,9,4,7,2.
    -> The numbers should be arranged in ascending order 1,2,4,7,9.
    -> The count of the numbers in 5 . So, the middle number is the third number.
    -> The median 4 as it is the third number of the given numbers.
if count of numbers is an even number, median is the average of the two middle values.

For example , if number are 3,7,10,15

    -> The median is 8.5 as the average of the two middle number(7,10) is 8.5 .



'''
# Source Code.

def list_num(num):
    list_a = []
    for i in num:
        list_a += [int(i)]
    return sorted(list_a)

def median_num(num):
    lenght = len(num)
    if lenght % 2 == 0:
        m = lenght //2
        sun = (num[m-1] + num[m])/22
        return sun


    else:
        return num[lenght//2]


num = input("Enter the number : ").split(",")
list_num = list_num(num)
result = median_num(list_num)
print(result)