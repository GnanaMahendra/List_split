'''
Give the list of N word. Write a program to print each word in a line.

example:
input:
    Banana Apple Pomegranate Strawberry Grapes Orange
output:
    Banana
    Apple
    Pomegranate
    Strawberry
    Grapes
    Orange
'''

word= input()

sentecnce = word.split()

for i in sentecnce:
    print(i)