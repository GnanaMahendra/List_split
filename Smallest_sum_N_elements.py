'''
Given Comma-separated number N ,Write a program to print the smallest possible sum with N numbers of the given Comma-separed number.

Example :
if the given comma-separated numbers are 2,10,9,6,5 and N =3
    - The ascending order of the given comma-separated numberis 2,5,6,9,10.
    - The smallest possible sum with 3 numbers will be the sum of the first 3 smallest numbers.
    - The first 3 smallest numbers sum id 13(2 + 5 +  6 = 13)
output : 13 

'''
def getting_list(num):
    getting_list = []
    for i in num:
        getting_list += [int(i)]
    return getting_list


num = input("Enter the comma-separated number :").split(",")
index = int(input())
result = getting_list(num)
result = sorted(result)
sun = sum(result[:index])
print("The sum of the N indexing sum : " + str(sun ))