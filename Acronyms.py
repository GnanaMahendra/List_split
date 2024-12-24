'''
Yiu are given some abbreviations as input. Write a program to print the acronyms separated by a dot(.) of those abbreviations.

sample (i/o)
 input:
    Indian Administrative Service
output:
    I.A.S
sample (i/o)
 input:
    Indian Administrative Service
output:
    I.A.S
sample (i/o)
 input:
    Very Important Person
output:
    V.I.P
'''
word = input().split()

acronyms_list = []
for i in word:
    acronyms_list += [i[0]]
print(".".join(acronyms_list))