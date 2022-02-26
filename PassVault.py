import tkinter
from tkinter import *
import sqlite3
import random
import string

#creating password function to generate 12 char string (upper and lower case with numbers) ---------------

def getPassword(size=12, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

password = getPassword()

#building table in sqlite3 ------------------

#connect to database and create cursor

conn = sqlite3.connect('vault.db')
c = conn.cursor()

#function for user to create database with button

def createTable ():
    c.execute("""CREATE TABLE vault (
        sitename TEXT
        username TEXT
        password TEXT
    )""")

    conn.commit()

    conn.close()

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


#when create table button is clicked        still need to add actually creation of table later ==========================

def tablePressed ():
    hideEl(instruct13)
    hideEl(instruct14)
    hideEl(instruct15)
    hideEl(createTblBtn)
    showEl(tableMade)


#start page gone function

def startGone(a, b, c, d, e, f, g, h, i, j, k):
    a.pack_forget()
    b.pack_forget()
    c.pack_forget()
    d.pack_forget()
    e.pack_forget()
    f.pack_forget()
    g.pack_forget()
    h.pack_forget()
    i.pack_forget()
    j.pack_forget()
    k.pack_forget()

#when generate button is pressed 

def genBtnClick():
    startGone(heading1, instruct11, instruct12, instruct13, instruct14,
     instruct15, space1, space2, genButton1, retButton1, createTblBtn)
    hideEl(tableMade)
    showEl(genTitle)
    showEl(nameLabel)
    showEntry(nameEntry)
    showEl(siteLabel)
    showEntry(siteEntry)
    showEl(subBtn)

#when submit button is pressed on g1

def hideg1():
    hideEl(genTitle)
    hideEl(nameLabel)
    hideEl(nameEntry)
    hideEl(siteLabel)
    hideEl(siteEntry)
    hideEl(subBtn)


def submitg1():
    username = nameEntry.get()
    site = siteEntry.get()
    #add username, site, password to database
    hideg1()
    showEl(genFinalMsg)
    showEl(passwordCopy)
    showEl(finishedGen)

#when submit button is pressed on r1

def retBtnClick():
    startGone(heading1, instruct11, instruct12, instruct13, instruct14,
     instruct15, space1, space2, genButton1, retButton1, createTblBtn)
    showEl(retTitle)
    showEntry(retSiteEntry)
    showEl(retSiteSubmit)

#creating gui ---------

window = tkinter.Tk()
window.geometry("450x300")
window.title("Password Generator and Vault")
window.configure(background = "black")

#start screen

heading1 = Label (window, text="Welcome to Cfugs's: The Vault!", bg="green", fg="white", font="none 12 bold")
showEl(heading1)
instruct11 = Label (window, text="Below, choose between Genterating a new password", bg="black", fg="white", font="none 9 bold")
showEl(instruct11)
instruct12 = Label (window, text="or Retrieveing one from the vault", bg="black", fg="white", font="none 9 bold")
showEl(instruct12)
space1 = Label (window, text="--------------------------------------------------", bg="black", fg="white", font="none 9 bold")
showEl(space1)
genButton1 = Button (window, text="Generate", width=10, command=genBtnClick)
showEl(genButton1)
retButton1 = Button (window, text="Retrieve", width=10, command=retBtnClick)
showEl(retButton1)
space2 = Label (window, text="--------------------------------------------------", bg="black", fg="white", font="none 9 bold")
showEl(space2)
instruct13 = Label (window, text="If this is your first time using the vault", bg="black", fg="white", font="none 9 bold")
showEl(instruct13)
instruct14 = Label (window, text="Please create a table by clicking the button below", bg="black", fg="white", font="none 9 bold")
showEl(instruct14)
instruct15 = Label (window, text="If youve already hit this button before, do not make a new table", bg="black", fg="white", font="none 9 bold")
showEl(instruct15)
createTblBtn = Button (window, text="Create Table", width=12, command=tablePressed)
showEl(createTblBtn)
tableMade = Label (window, text="Table created successfully!", bg="black", fg="white", font="none 9 bold")
hideEl(tableMade)

#g1

genTitle = Label (window, text="Please fill out boxes below", bg="green", fg="white", font="none 12 bold")
hideEl(genTitle)
nameLabel = Label(window, text = 'Username', font=('none',10, 'bold'))
hideEl(nameLabel)
nameEntry = Entry(window, width=20, font=('calibre',10,'normal'))
hideEl(nameEntry)
siteLabel = Label(window, text = 'Site or app name', font = ('none',10,'bold'))
hideEl(siteLabel)
siteEntry = Entry(window, width=20, font = ('none',10,'bold'))
hideEl
subBtn = Button(window, text = 'Submit', command=submitg1)
hideEl(subBtn)

#g2

genFinalMsg = Label (window, text=f"Your password is saved in the vault! Your password is {password}", bg="green", font = ('none',10,'bold'))
hideEl(genFinalMsg)
passwordCopy = Button (window, text="Copy password to clipboard", command=copyPassClip)
hideEl(passwordCopy)
finishedGen = Button (window, text="Finished", command=finished)
hideEl(finishedGen)

#r1

retTitle = Label (window, text="Please enter the sitename for password.",  bg="green", font = ('none',12,'bold'))
hideEl(retTitle)
retSiteEntry = Entry (window, width=25)
hideEl(retSiteEntry)
retSiteSubmit = Button (window, text="submit")


window.mainloop()



