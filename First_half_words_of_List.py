'''
Given space-separated words, write a program that creates a list using space-separated words and prints the first half of the words in the list as a new list.
Note : If the given number of words is an odd number, add one to it such that it becomes an even number and count half of the number of words

sample (i/o)

input:
    python java c html
output:
    ['python', 'java']
Sample (i/p)
input:
    apple mango orange grapes kiwi
output:
    ['apple', 'mango', 'orange']
'''
word = input()
word = word.split()
if len(word) % 2 == 0:
    a =int(len(word)/2)
else:
    a =int(len(word)/2)+1
print(word[:a])