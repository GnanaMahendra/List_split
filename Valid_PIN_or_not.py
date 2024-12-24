'''
write  Function with the name validate_atm_pin_code that takes a word as an argument
ATM PIN is considered valid only if the given word contains
    - Exactly 4 or 6 characters
    - All the characters should digits

sample (i/p)
input:
    9999
output:
    Valid PIN Code
sample (i/p)
Input :
    12dfa2
output:
    Invalid PIN Code

'''

def validate_atm_pin_code(pin):
    if pin.isdigit() and (len(pin) == 4 or (len(pin) == 6)):
        print("Valid PIN Code")
    else:
        print("Invalid PIN Code")

        
pin = input()
validate_atm_pin_code(pin)