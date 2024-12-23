'''
Check First Letter and Last Letter of Word
Given space-separated words, write a program to check if the first letter and last letter of each word are the same.
Note : "Consider both uppercase and lowercase letters as the same."

sample (i/o)
Input
    water Noon river
Output
    False
    True
    True
sample (i/o)
Input
    eat play dance work label
Output
    False
    False
    False
    False
    True
'''
word = input()
word = word.split()

for i in word:
    print(i[0] == i[-1])