'''
Write a function with the name calculate_bill that takes the bill amount as an argument.
---> If the bill amount is less than 500, the discount should be 5%.
---> If the bill amount is greater than or equal to 500 and less than 2500, the discount should be 10%.
---> If the bill amount is greater than or equal to 2500, the discount should be 20%. 
Calculate the bill amount with the appropriate discount and print it.

sample (i/o)

Input:
    1500
Output:
    1350.5
Sample (i/o)

Input:
    250
Output:
    237.5

'''
def calculate_bill(amount):
    # Complete this function
    if amount < 500:
        gst = amount - (amount* (5/100))
        print(gst)
    elif amount >= 500 and amount < 2500:
        gst = amount - (amount * (10/100))
        print(gst)
    elif amount >= 2500:
        gst = amount - (amount * (20/100))
        print(gst)
        
amount = int(input())
# Call the calculate_bill function
calculate_bill(amount)