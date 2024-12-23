'''Given space-separated words, write a program that creates a list using space-separated words and prints the first half of the words in the list as a new list.
Note : If the given number of words is an odd number, add one to it such that it becomes an even number and count half of the number of words

sample (i/o)

input:
    38 -49 52 -66 71 89 88 -23 41 98
output:
    [38, -49, 52, -66, 71]
Sample (i/p)
input:
    1 3 9 0 8 2 7
output:
    [1, 3, 9, 0]

'''
num = input()
num = num.split()
if len(num)%2 == 0:
    a = (len(num)//2)
else:
    a = (len(num)//2)+1
list_out =[]
for i in range (a):
    list_out += [int(num[i])]
print(list_out)