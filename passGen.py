from re import sub
import string
import random
import tkinter
from tkinter import *
from storage import vaultFunc



buttonClick = 0


def getPassword(size=12, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

password = getPassword()


def clickGen(a, b, c, d, e, f):
    buttonClick = 1
    a.pack()
    b.pack()
    c.pack()
    d.pack()
    e.pack()
    f.pack()
    

def clickRet():
    buttonClick = 2

def clearStart(x, y, z, c, l, o):
    x.pack_forget()
    y.pack_forget()
    z.pack_forget()
    c.pack_forget()
    l.pack_forget()
    o.pack_forget()

def submit():
    username = name_entry.get()
    site=site_entry.get()
    vaultFunc(username, site, password)
    clearGenPageTwo(genTitle, name_label, name_entry, site_label, site_entry, sub_btn)
    genFinal(genFinalMsg, passwordCopy, finishedGen)


def clearGenPageTwo(a, b, c, d, e, f):
    a.pack_forget()
    b.pack_forget()
    c.pack_forget()
    d.pack_forget()
    e.pack_forget()
    f.pack_forget()
   
def genFinal(c, f, j):
    c.pack()
    f.pack()
    j.pack()

def copyPassClip():
    window.clipboard_clear()
    window.clipboard_append(password)


def finished():
    window.destroy()


window = tkinter.Tk()
window.geometry("450x300")
window.title("Password Generator and Vault")
window.configure(background = "black")
heading = Label (window, text="Welcome to Cfugs Password Generator and Vault!", bg="green", fg="white", font="none 12 bold")
heading.config(anchor=CENTER)
heading.pack()
instruct1 = Label (window, text="Below, choose between Genterating a new password", bg="black", fg="white", font="none 9 bold")
instruct1.config(anchor=CENTER)
instruct1.pack()
instruct2 = Label (window, text="or Retrieveing one from the vault", bg="black", fg="white", font="none 9 bold")
instruct2.config(anchor=CENTER)
instruct2.pack()
space = Label (window, text="--------------------------------------------------", bg="black", fg="white", font="none 9 bold")
space.config(anchor=CENTER)
space.pack()
genButton = Button (window, text="Generate", width=10, command=lambda:[clearStart(heading, instruct1, instruct2, space, retButton, genButton), clickGen(genTitle, name_label, name_entry, 
site_label, site_entry, sub_btn)])
genButton.config(anchor=CENTER)
genButton.pack()
retButton = Button (window, text="Retrieve", width=10, command=lambda:[clearStart(heading, instruct1, instruct2, space, retButton, genButton), clickRet()])
retButton.config(anchor=CENTER)
retButton.pack()


genTitle = Label (window, text="Please fill out boxes below", bg="green", fg="white", font="none 12 bold")
genTitle.config(anchor=CENTER)
genTitle.pack_forget()
name_label = Label(window, text = 'Username', font=('calibre',10, 'bold'))
name_label.config(anchor=CENTER)
name_label.pack_forget()
name_entry = Entry(window, width=20, font=('calibre',10,'normal'))
name_entry.config(justify=CENTER)
name_entry.pack_forget()
site_label = Label(window, text = 'Site or app name', font = ('calibre',10,'bold'))
site_label.config(anchor=CENTER)
site_label.pack_forget()
site_entry = Entry(window, width=20, font = ('calibre',10,'normal'))
site_entry.config(justify=CENTER)
site_entry.pack_forget()
sub_btn = Button(window, text = 'Submit', command = submit)
sub_btn.config(anchor=CENTER)
sub_btn.pack_forget()

genFinalMsg = Label (window, text=f"Your password is saved in the vault! Your password is {password}", bg="green", font = ('calibre',10,'normal'))
genFinalMsg.config(anchor=CENTER)
genFinalMsg.pack_forget()
passwordCopy = Button (window, text="Copy password to clipboard", command=copyPassClip)
passwordCopy.config(anchor=CENTER)
passwordCopy.pack_forget()
finishedGen = Button (window, text="Finished", command=finished)
finishedGen.config(justify=CENTER)
finishedGen.pack_forget()

window.mainloop()
        



