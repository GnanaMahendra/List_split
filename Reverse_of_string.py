#Revers of string using recursion 

def get_rev_of_str(string):
    if not string:
        return ""
    else:
        return string[-1] + get_rev_of_str(string[:-1])


string = input("Enter the String : \t")
print("\n" + get_rev_of_str(string))