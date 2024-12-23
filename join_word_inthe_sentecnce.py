'''
Given a sentence word . the word in the sentence word are separated by a space.
Write a program that print string by joining the words in the sentence word woth the dot(.).

sample (i/o)
input:
    This is a program
output:
    This.is.a.program

sample (i/o)
input:
    Dreams come true
output:
    Dreams.come.true

'''

word = input()

split_word = word.split()
split_word = ".".join(split_word)
print(split_word)