# REVERSE A STRING

def reverse_string(string):
    if len(string) < 1:
        print(f"\nyour string '{string}' is too small to perform this operation. We don't do that here.")
        return
    elif string.isdigit() == True:
        print(f"\nyour string '{string}' is a number. We don't do that here.")
        return
    else:
        rString = string[::-1]
        print(f"\nYour reversed string is: {rString}")
        return rString

def menu():
    print("\nWelcome to string reversal -- You can reverse almost ")
    string = input("Enter string to reverse here: ")
    reverse_string(string)
    
menu()