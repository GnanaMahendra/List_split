'''
Write program to recursively find the Nth term in the Fibonacci series.
A fibonacci sequence are 0and 1. All other terms are obtained by adding the preceding to terms.
 Example:

Input :
    5
 
 Term | number
   0  |  0
   1  |  1
   2  |  1
   3  |  2
   4  |  3
   5  |  5
Output : 5

'''
def fibonacci(num):
    if num <=1:
        return num
    else:
        return fibonacci(num-1) + fibonacci (num-2)


num = int(input())
result = fibonacci (num)
print(result)
