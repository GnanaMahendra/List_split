'''
For this problem, the prefilled code will contain a function. Write a program to count the number of uppercase and lowercase letters in the given word

Sample (I/O)
Input :
    MasTer
Output :
    2
    4

Sample (I/O)

Input :
   FOUNDATIONS
Output :
    11
    0
'''
def count_of_lowercase_and_uppercase_letters(arg_1):
    # Complete this function
    count_of_lowercase = 0
    count_of_uppercase =0
    for i in word:
        if i.islower():
            count_of_lowercase +=1
        elif i.isupper():
            count_of_uppercase +=1
    print(count_of_uppercase)
    print(count_of_lowercase)


word = input()
# Call the count_of_lowercase_and_uppercase_letters function
count_of_lowercase_and_uppercase_letters(word)
