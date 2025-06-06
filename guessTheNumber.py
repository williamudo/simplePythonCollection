# Computer Guessing Game

# need to import random
import random


# PRE : NONE
#POST : GENERATE AND RETURN RANDOM COMPUTER NUMBER. AS WELL AS USER INPUT
def numGenerator():
    return random.randint(1, 10)



# PRE : USER AND COMPUTER NUMBER
# POST : CHECK TO SEE IF COMPUTER NUMBER MATCHES USER NUMBER
def numChecks(cmptrNum):
    guessCtr = 0
    while guessCtr < 3:
        usrNum = int(input("Guess number: "))
        if cmptrNum == usrNum:
            print("You guessed the number")
            return
        
        else:
            print("Wrong. Guess again\n")
            guessCtr += 1
            

    
    print(f"You've guessed enough. the correct answer was {cmptrNum}.")

        

# PRE : NONE ?
# POST : HANDLES USER INTERACTION AS WELL AS PREVIOUS FUNCTION CALLS
def menu():
    usrChoice = ""
    print("\nWelcome to the Number Guessing Game\n")
    cmptrNum = numGenerator()
    while usrChoice.lower() != "N":
        numChecks(cmptrNum)
        usrChoice = input("Would you like to play again? (Y/N): ")
        if usrChoice == "y":
            continue
        else:
            print("Have a good day")
            break

menu()