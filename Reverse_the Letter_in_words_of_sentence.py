'''
Given a sentence, Write a program to reverse yhr letters in words of the sentence.

sample(i/o)
input:
    The cat is on the mat.
output:
    ehT tac si no eht .tam

sample(i/o)
input:
    Have a nice weekend.
output:
    evaH a ecin .dnekeew

'''
word = input()

word = word.split()

words = []
for i in word:
    words += [i[::-1]]
words = ",".join(words)
print(words)