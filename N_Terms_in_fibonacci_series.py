'''
Write a program to recursively create a list of n Fibonacci terms.
a Fibonacci sequence is the integer sequence of 0,1,1,2,3,5,8....
The first two terms are 0 and 1 . All other terms are obtained by adding the preceding two terms.

Example :
Input :
    Enter the number :  6
Output :
    [0, 1, 1, 2, 3, 5]
'''

def  fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci (n-2)
    

def get_fibonacci_terms(num):
    term = []
    for i in range(num):
        fib_num = fibonacci(i)
        term.append(fib_num)
    return term

num = int(input("Enter the number :  5"))

result = get_fibonacci_terms (num)
print(result)