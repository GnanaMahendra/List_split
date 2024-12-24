'''
Write a function with the name fizz_buzz that takes a number as an argument.

    -> If the number is divisible by 3, it should return "Fizz".
    -> If it is divisible by 5, it should return "Buzz".
    -> If it is divisible by both 3 and 5, it should return "FizzBuzz".
    -> Otherwise, it should return the same number.

Sample (I/O)
input:
    20
Output:
    Buzz

Sample(I/O)

Input:
    7
Output :
    7
'''

def fizz_buzz(number):
    # Complete this function
    if number %3 == 0 and number %5 != 0:
        print("Fizz")
    elif number %5 == 0 and number %3 != 0:
        print("Buzz")
    elif number % 5 == 0 or number % 3 == 0:
        print("FizzBuzz")
    else:
        print(number)


number = int(input())
# Call the fizz_buzz function
fizz_buzz(number)