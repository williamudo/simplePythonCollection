# REPLACE ONE STRING WITH ANOTHER

def replace_string(original, old, new):
    if old not in original:
        print(f"\n'{old}' was not found in '{original}' ")
        return original
    
    else:
        updated = original.replace(old, new)
        print(f"\nYour new string looks like: {updated}")
        return updated


def menu():
    print("Welcome to string replacement")
    print()

    orig_string = input("Write your orginal string here: ")
    old_string = input("Enter letter/word you want to change: ")
    new_string = input("Write letter/word you want to change to: ")
    
    replace_string(orig_string, old_string, new_string)

menu()