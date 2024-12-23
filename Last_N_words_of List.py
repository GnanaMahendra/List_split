'''
Given space-separated words S and a number N ,Write a program that creates a list using space-separated words and prints the last N words of the list in reverse order.

sample(i/o)
input:
    This is my favourite cookie
    4
output:
    ['cookie', 'favourite', 'my', 'is']

sample(i/o)
input:
    a piece of cake
    2
output:
    ['cake', 'of']
'''
sentence = input()
number = int(input())

words = sentence.split()

words_list = words[-number:]
resultant_list = words_list[::-1]

print(resultant_list)