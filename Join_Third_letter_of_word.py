'''
Given a sentence s. The word in the sentence s are separated by a space.
Write a program that prints a new string by joining the third letter of each word in the sentence woth the comma(,).

sample (i/o)

input:
    Being More Productive
output:
    i,r,o

sample (i/o)

input:
    Python Course
output:
    t,u
'''
word = input()

word = word.split()

list_out =[]

for i in word:
    list_out += [i[2] ]
list_out = ",".join(list_out)

print(list_out)