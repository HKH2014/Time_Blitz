import csv, random, sys, time, os
score = 0


def make_account():

    #before a user will be able to make an account, the managers of explore learning would need to give permission
    #Permission can only be given by the two of explore's manager's via their employee code.
    codex = input("Enter manager's employee code to proceed:")
    if codex == "78356" or "13576":
        next_steps()
    elif codex != "78356" or "13576": # its not registering this for some reason
        #quit("Invalid code. Goodbye")
        #sys.exit("Invalid code. Goodbye")
        print("Invalid code. Goodbye")
        exit()
        

def next_steps():
    # The program is collecting data regarding the player
    # This will help create a username
    # It will also allow the program to tailor the game towards the player itself
    # i.e. The difficulty of the game's questions and time allowed
    forename = input("Please enter player's forename:")
    surname = input("Please enter player's surname:")
    birth_year = int(input("Please enter player's full year of birth:"))
    time = int(input("Please enter the time limit (seconds) for the player:"))
    level = input("What level? KS1, KS2 OR KS3")

    #creating a username by manipulainng the strings using the information already given
    username = forename + surname + str(birth_year)
    print ("\n\
Player's username:" , username)

    password = input("\n\
Please enter new password:")
    password_Verification = input("Please re-enter password:")

#This loop here makes sure that the password is the same both times
#If both passwords are not the same, it will keep asking to re-fill unitl they both match
    while password != password_Verification:
        print("\n\
Passwords don't match. Please re-enter password:")
        password = input("Please enter new password:")
        password_Verification = input("Please re-enter password:")
    
#This print statement is the confirmation that the sign up has been sucsessfull
    print("\n\
Thank you for signing up. Please re-load page to log in.")

#creating/opening a file using the append mode to store the names of the users
#Every row will have a detail about the player in the order username, password ect.
#Appending so it just adds extra detail about they player or creates a new record if no details exist.
    with open ("UserDetails.csv" , "a" , newline="")as UserInfo:
        UserInfoWriter = csv.writer(UserInfo)
        UserInfoWriter.writerow([username, password,surname,forename,birth_year,time,level,score])
    UserInfo.close()

    return username
    return score




def Menu (): # code starts here

# The menu will introduce the player to the program by taking login details
    welcome = """Time Blitz: 2021

Let's see what you've got.

First, the boring stuff...
"""
    
    #Due to this part here, The code will print the welcome with a type writing effect
    #It will do so, character by character rather than all at once
    #The time.sleep function will determine the writing speed.
    for char in welcome:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
   
    haveaccount = input("Do you already have an account with us?").lower()

    if haveaccount == "yes":
        print("\n\
Great, We need your username and password:")
        #Unfortunantly I was unable to use the getpass module to hide my password as my device hasn't got the resources
        #However, if i did, it would be written like this:
        #password = getpass.getpass("Enter passowrd")
        username = input("\n\
Please enter username:")
        password = input("Please enter password:")

    # checking that player is an authenticated player by reading the lines in the external CSV file

        StoreUserDetails = []
        with open ("UserDetails.csv", "r" , newline="") as UserInfo:
            person  = csv.reader(UserInfo)
            
            #Here, the program is writing details 
            for row in person:
                personA = row[0]
                StoreUserDetails.append(personA)
        UserInfo.close()
            
        if username in StoreUserDetails: # it won't let me in irregardless
            
            print("Great. You're all set up!")
            #Game()
            #make a call to the subrountine where the game is played 

        else:
            print("\n\
Thats not an authenticated user. Please reload page.")
            
    #providing user with option to sign up should they want to make an account
    # if yes, it jumps to the subroutine that makes accounts
    else:
        sign_up = input("Would you like to sign up?").lower()
        if sign_up == "yes":
            make_account()

        else:
            print("Not a problem, have a good day.")

Menu()
