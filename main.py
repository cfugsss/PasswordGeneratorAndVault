import string
import random


vault = open('data.txt', 'a')

def getPassword(size=12, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

print("---------------------------------------------------------------------------")
print("                                                                           ")
print("Welcome to cfugs password generator!")
print("                                                                           ")
print("In the prompt below type 1 for generating a new password or 2 for help :")
choice = int(input("Enter selection: "))

def main():
    if choice != 1 and choice != 2:
        print("---------------------------------------------------------------------------")
        print("                                                                           ")
        print("Please restart and type either 1 or 2 in the first prompt!")
        print("                                                                           ")
        print("---------------------------------------------------------------------------")
    if choice == 1:
        password = getPassword()
        app = input("Enter name of app or site are you generating a password for: ")
        username = input("Enter your username/email for site or app: ")
        vault.write("\n")
        vault.write(f"|| Your password for {app} is {password}. Your username/email is {username}. ||")
        print("---------------------------------------------------------------------------")
        print("                                                                           ")
        print("Your password was generated!")
        print("                                                                           ")
        print("Your credentials are stored in the data file!")
        print("                                                                           ")
        print("---------------------------------------------------------------------------")
    if choice == 2:
        print("---------------------------------------------------------------------------")
        print("                                                                           ")
        print("                           HELP MANUAL                                     ")
        print("                                                                           ")
        print("To access your password or username access the data.txt file in the folder")
        print("where this script is saved on your computer")
        print("                                                                           ")
        print("---------------------------------------------------------------------------")
        print("                                                                           ")
        print("To generate a new password, restart the program and type 1 in the first")
        print("prompt in the terminal.")
        print("                                                                           ")
        print("---------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------")
        print("                                                                           ")
        print("To find your password in the data.txt file easily, press control F")
        print("on your keyboard, then type your username or app/site name in the ")
        print("pop up box, the line with your password will be highlighted")
        print("                                                                           ")
        print("---------------------------------------------------------------------------")
        
main()
    
#still doesnt work if you enter a string in the first input
#but im just using this for myself so does it really matter???1