'''
Write a program remove the nth last element in the list.

Example :
Input :
    5
Output :
    ['Python', 'C', 'Java', 'Ruby', 'C++', 'CSS', 'HTML', 'Bash', 'Perl']

'''



programming_languages = ['Python', 'C', 'Java', 'Ruby', 'C++', 'CSS', 'HTML', 'Bash', 'Perl', 'R', 'Swift', 'SQL', 'PHP', 'JavaScript']
n = int(input())# Write your code here
for i in range(n):
    programming_languages.pop()
print(programming_languages)   