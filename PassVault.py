import tkinter as tk
from tkinter import *
import random
import string
import sqlite3

#creating password function to generate 12 char string (upper and lower case with numbers) ---------------

def getPassword(size=12, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

password = getPassword()

#creating gui ---------

window = tk.Tk()
window.geometry("450x300")
window.title("Password Manager")
window.configure(background = "LightSkyBlue3")

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
    username = nameEntry.get()
    site = siteEntry.get()
    conn = sqlite3.connect("vault.db")
    with conn:
        cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Users (id integer PRIMARY KEY AUTOINCREMENT, Sitename TEXT,Username TEXT, Password TEXT)")
    cursor.execute("INSERT INTO users (Sitename,Username,Password)" "VALUES(?,?,?)", (site, username, password))
    conn.commit()
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
        siteShow = Label (window, text=f"Sitename: {ans[0]}", bg="LightSkyBlue3", fg="black", font="none 15 bold")
        showEl(siteShow)
        userShow = Label (window, text=f"Username: {ans[1]}", bg="LightSkyBlue3", fg="black", font="none 15 bold")
        showEl(userShow)
        passShow = Label (window, text=f"Password: {ans[2]}", bg="LightSkyBlue3", fg="black", font="none 15 bold")
        showEl(passShow)
        alertBox = Label (window, text="Password copied to clipboard!")
        showEl(alertBox)
        

        

    
    
        





#start screen

heading1 = Label (window, text="Welcome to The Vault!", bg="LightSkyBlue3", fg="black", font="none 15 bold")
showEl(heading1)
instruct11 = Label (window, text="Below, choose between Genterating a new password", bg="LightSkyBlue3", fg="black", font="none 12 bold")
showEl(instruct11)
instruct12 = Label (window, text="or Retrieveing one from the vault", bg="LightSkyBlue3", fg="black", font="none 12 bold")
showEl(instruct12)
genButton1 = Button (window, text="Generate", width=15, height= 3, command=generate)
showEl(genButton1)
retButton1 = Button (window, text="Retrieve", width=15, height = 3, command=retrieve)
showEl(retButton1)

# gen1

genTitle = Label (window, text="Please fill out boxes below", bg="LightSkyBlue3", fg="black", font="none 12 bold")
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

genFinalMsg = Label (window, text=f"Your password is saved in the vault! Your password is {password}", bg="LightSkyBlue3", fg="black", font = ('none',10,'bold'))
hideEl(genFinalMsg)
passwordCopy = Button (window, text="Copy password to clipboard", command=copyPassClip)
hideEl(passwordCopy)
finishedGen = Button (window, text="Finished", command=finished)
hideEl(finishedGen)

#ret 1

retTitle = Label (window, text="Please enter the sitename for password.",  bg="LightSkyBlue3", fg="black", font = ('none',15,'bold'))
hideEl(retTitle)
retSiteEntry = Entry (window, width=25)
hideEl(retSiteEntry)
retSiteSubmit = Button (window, text="submit", command=retrieveAcc)

#ret 2




window.mainloop()