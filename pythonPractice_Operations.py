# COMPARE TWO STRINGS USING OPERATIONS

def check_string(str1, str2):
    if str1 == str2:
        return True
    else:
        return False

def menu():
    print("\nCheck and see if two strings are equal!")
    print("If the strings are equal, the function retutns True. Otherwise, False.")

    str1 = input("\nWrite a string here: ")
    str2 = input("Wtite another string here: ")
    
    print(f"\n{check_string(str1, str2)}")

menu()





        