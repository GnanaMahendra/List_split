'''
Write a program add the word into the list using the Extend.
Example :

Input :
    gnana mahendra sai mahi
Output :
    ['gnana', 'mahendra' , 'sai' , 'mahi']

'''

l = []
word= input().split()
l.extend(word)
print(l)
