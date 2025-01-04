'''
Given a sentence s thar contains space-separated words, write a program to print a list of word that do not start with the lowercase latter "a".
Example :
Input :
    Enter the sentence :  The favorite dish of all ages was apple pie

Output :
    ['The', 'favorite', 'dish', 'of', 'was', 'pie']
'''

word = input("Enter the sentence :  ").split()

new_list = []

for i in word:
    if i.startswith("a"):
        continue
    new_list.append(i)
print(new_list)