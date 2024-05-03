from tkinter import*
import string
import secrets
import random
import pyperclip

def generator():
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    all=upper+lower+digits+punctuation
    password_len=int(length_Box.get())
    part1 = round(password_len * (30 / 100))
    part2 = round(password_len * (20 / 100))
    
    password=""
    for i in range(part1):
        password += secrets.choice(upper)
        password += secrets.choice(digits)

    for i in range(part2):
        password += secrets.choice(punctuation)
        password += secrets.choice(lower)

    passwordField.insert(0,password)

def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

# Build Window

root = Tk() 
root.geometry("265x310")
mycolor='magenta2'
root.config(bg=mycolor)
choice=IntVar()
Font=('arial',13,'bold')

passwordlabel=Label(root,text='Password Generator',font=('Helvetica',18,'bold'),bg='yellow',fg='red')
passwordlabel.grid(pady=10)                                                # To see the label on the screen

lengthlabel=Label(root,text=" Provide password length",font=('Segoe Script',14),bg='blue',fg='light yellow')
lengthlabel.grid()

length_Box=Spinbox(root,from_=6,to_=24,font=Font,width=5,wrap=True)
length_Box.grid(pady = 5)

generateButton=Button(root,text='Generate',font=(Font,10,'bold'),bg='gold',command=generator,relief= RAISED)
generateButton.grid(pady=15)

passwordField=Entry(root,width=20,bd=2,font=Font)
passwordField.grid()

copyButton=Button(root,text='Copy to Clipboard',font=(Font,10,'bold'),bg='aqua',command=copy,relief=GROOVE)
copyButton.grid(pady=15)

mylabel=Label(root,text='Created By: Piyush Gupta',font=('Segoe Script',10,'bold'),bg='lawn green',fg='red')
mylabel.grid(pady=10)

root.mainloop()