__author__ = 'verasraul'




def printMenu():
    print("\nWelcome, what would you like to do?")
    print("\t[1] Enter Grades")
    print("\t[2] Remove Student")
    print("\t[3] Get Student Average")
    print("\t[4] Exit")


def mainMenu():
    userInApp = True
    while userInApp is True:
        printMenu()
        userSelection = input("What would you like to do today? (Enter a number).")
        if userSelection == "4":
            exitprompt = input("You choose to exit. Are you sure? (Enter Y for yes and N for no).")
            if exitprompt == "y" or exitprompt == "y".upper():
                print("Exiting Grading System.")
                userInApp = False
            elif exitprompt == "n" or exitprompt == "n".upper():
                print("Please choose an option.")


mainMenu()