'''
Write a program to compute the frequency of characters other then space.

Sample I/O

Input : 
Pop up
Output :
o: 1
p: 3
u: 1

Input:
Tic tac Toe
Output :

a: 1
c: 2
e: 1
i: 1
o: 1
t: 3
'''
def frequency_list(num):
    num= num.lower()
    num_set = set(num)
    num_set.discard(" ")
    num_set= sorted(num_set)
    for i in num_set:
        msg = "{}: {}"
        print(msg.format(i, num.count(i)))



num = input()
frequency_list(num)
