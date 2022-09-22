from email.mime import image
import tkinter as tk
from tkinter import *
import random
import string
import sqlite3
import PIL
from PIL import ImageTk, Image

#creating password function to generate 12 char string (upper and lower case with numbers) ---------------

def getPassword(size=12, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

password = getPassword()

#creating gui ---------



window = tk.Tk()
window.geometry("450x300")
window.title("Password Manager")
# window.configure(background = "vaultbg.jpg")

backg = Image.open("vaultbg.jpg")
bg = ImageTk.PhotoImage(backg)
background_label = tk.Label(window, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



#finished button function to close window

def finished():
    window.destroy()

#function to copy password to clipboard

def copyPassClip():
    window.clipboard_clear()
    window.clipboard_append(password)


#function to center and pack element

def showEl(x):
    x.config(anchor=CENTER)
    x.pack()

#function to hide element

def hideEl(x):
    x.pack_forget()

#function to show entries

def showEntry(x):
    x.config(justify=CENTER)
    x.pack()

def generate():
    hideEl(heading1)
    hideEl(instruct11)
    hideEl(instruct12)
    hideEl(genButton1)
    hideEl(retButton1)
    showEl(genTitle)
    showEl(nameLabel)
    showEntry(nameEntry)
    showEl(siteLabel)
    showEntry(siteEntry)
    showEl(subBtn)

def retrieve():
    hideEl(heading1)
    hideEl(instruct11)
    hideEl(instruct12)
    hideEl(genButton1)
    hideEl(retButton1)
    showEl(retTitle)
    showEntry(retSiteEntry)
    showEl(retSiteSubmit)

def backHomeGen():
    hideEl(genFinalMsg)
    hideEl(passwordCopy)
    hideEl(finishedGen)
    hideEl(backtoHome)
    showEl(heading1)
    showEl(instruct11)
    showEl(instruct12)
    showEl(genButton1)
    showEl(retButton1)

def getPassword():
    hideEl(genTitle)
    hideEl(nameLabel)
    hideEl(nameEntry)
    hideEl(siteLabel)
    hideEl(siteEntry)
    hideEl(subBtn)
    showEl(genFinalMsg)
    showEl(passwordCopy)
    showEl(finishedGen)
    showEl(backtoHome)
    username = nameEntry.get()
    site = siteEntry.get()
    conn = sqlite3.connect("vault.db")
    with conn:
        cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Users (id integer PRIMARY KEY AUTOINCREMENT, Sitename TEXT,Username TEXT, Password TEXT)")
    cursor.execute("INSERT INTO users (Sitename,Username,Password)" "VALUES(?,?,?)", (site, username, password))
    conn.commit()
    cursor.close()
    # with conn:
    #     cursor.execute("SELECT * FROM users")
    #     print(cursor.fetchall())

def retrieveAcc():
    hideEl(retTitle)
    hideEl(retSiteEntry)
    hideEl(retSiteSubmit)
    sitename = retSiteEntry.get()
    conn = sqlite3.connect("vault.db")
    with conn:
        cursor = conn.cursor()
    with conn:
        cursor.execute(f'''
                    SELECT Sitename, Username, Password
                    FROM Users
                    WHERE Sitename="{sitename}"
                    ''')
        ans = cursor.fetchone()
        window.clipboard_clear()
        window.clipboard_append(str(ans[2]))
        def backHomeRet():
            hideEl(siteShow)
            hideEl(userShow)
            hideEl(passShow)
            hideEl(alertBox)
            hideEl(backHome)
            showEl(heading1)
            showEl(instruct11)
            showEl(instruct12)
            showEl(genButton1)
            showEl(retButton1)
            
        siteShow = Label (window, text=f"Sitename: {ans[0]}", bg="grey50", fg="black", font="none 15 bold")
        showEl(siteShow)
        userShow = Label (window, text=f"Username: {ans[1]}", bg="grey50", fg="black", font="none 15 bold")
        showEl(userShow)
        passShow = Label (window, text=f"Password: {ans[2]}", bg="grey50", fg="black", font="none 15 bold")
        showEl(passShow)
        alertBox = Label (window, text="Password copied to clipboard!")
        showEl(alertBox)
        backHome = Button (window, text="Back Home", command=backHomeRet)
        showEl(backHome)

        cursor.close()
        



#start screen

heading1 = Label (window, text="Welcome to The Vault!",bg="grey42", fg="black", font="none 15 bold")
showEl(heading1)
instruct11 = Label (window, text="Below, choose between Genterating a new password", bg="grey42", fg="black", font="none 12 bold")
showEl(instruct11)
instruct12 = Label (window, text="or Retrieveing one from the vault", bg="grey42", fg="black", font="none 12 bold")
showEl(instruct12)
genButton1 = Button (window, text="Generate", width=15, height= 3, command=generate)
showEl(genButton1)
retButton1 = Button (window, text="Retrieve", width=15, height = 3, command=retrieve)
showEl(retButton1)

# gen1

genTitle = Label (window, text="Please fill out boxes below", bg="grey42", fg="black", font="none 12 bold")
hideEl(genTitle)
nameLabel = Label(window, text = 'Username', fg="black", font=('none',15, 'bold'))
hideEl(nameLabel)
nameEntry = Entry(window, width=20, font=('none',12,'bold'))
hideEl(nameEntry)
siteLabel = Label(window, text = 'Site or app name', font = ('none',12,'bold'))
hideEl(siteLabel)
siteEntry = Entry(window, width=20, font = ('none',12,'bold'))
hideEl
subBtn = Button(window, text = 'Submit', command=getPassword)
hideEl(subBtn)

#gen 2

genFinalMsg = Label (window, text=f"Your password is saved in the vault! Your password is {password}", bg="grey42", fg="black", font = ('none',10,'bold'))
hideEl(genFinalMsg)
passwordCopy = Button (window, text="Copy password to clipboard", command=copyPassClip)
hideEl(passwordCopy)
finishedGen = Button (window, text="Finished", command=finished)
hideEl(finishedGen)
backtoHome = Button (window, text="Back Home", command=backHomeGen)
hideEl(backtoHome)

#ret 1

retTitle = Label (window, text="Please enter the sitename for password.",  bg="grey42", fg="black", font = ('none',15,'bold'))
hideEl(retTitle)
retSiteEntry = Entry (window, width=25)
hideEl(retSiteEntry)
retSiteSubmit = Button (window, text="submit", command=retrieveAcc)


window.mainloop()