import tkinter as tk
import csv

root = tk.Tk()
root.title("Contact Book")
root.geometry("250x340")
root.config(bg = "salmon4")

fname_label = tk.Label(root, text="Enter First Name :")
fname_label.grid(row=0, column=0)
fname_entry = tk.Entry(root,bg = "peach puff")
fname_entry.grid(row=0, column=1)

lname_label = tk.Label(root, text="Enter Last Name :")
lname_label.grid(row=1, column=0,pady =5)
lname_entry = tk.Entry(root,bg = "peach puff")
lname_entry.grid(row=1, column=1)

phone_label = tk.Label(root, text="Enter Phone Number :")
phone_label.grid(row=2, column=0)
phone_entry = tk.Entry(root,bg = "peach puff")
phone_entry.grid(row=2, column=1)

email_label = tk.Label(root, text="Enter Email :")
email_label.grid(row=3, column=0,pady =5)
email_entry = tk.Entry(root,bg = "peach puff")
email_entry.grid(row=3, column=1)

address_label = tk.Label(root, text="Enter Address :")
address_label.grid(row=4, column=0)
address_entry = tk.Entry(root,bg = "peach puff")
address_entry.grid(row=4, column=1)

def save_contact():
    fname = fname_entry.get()
    lname = lname_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    info = [fname, lname, phone, email, address]
    with open('info.csv', 'a', newline="") as w:
        cw = csv.writer(w)
        cw.writerow(info)
    fname_entry.delete(0, tk.END)
    lname_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

save_button = tk.Button(root, text="Save",bg = "lawn green",command=save_contact)
save_button.grid(row=5, column=0,pady =5)

cancel_button = tk.Button(root, text="Cancel",bg = "red",command=root.destroy)
cancel_button.grid(row=5, column=1)

search_label = tk.Label(root, text="Search by Last name:")
search_label.grid(row=6, column=0)
search_entry = tk.Entry(root,bg="peach puff")
search_entry.grid(row=6, column=1)

search_output = tk.Text(root, height=5, width=30)
search_output.grid(row=8, column=0, columnspan=2)

def search_contact():
    search_text = search_entry.get()
    with open('info.csv', 'r') as r:
        pg = csv.reader(r)
        for i in pg:
            if i[1] == search_text:
                search_output.insert(tk.END, f"First Name: {i[0]}\nLast Name: {i[1]}\nPhone Number: {i[2]}\nEmail: {i[3]}\nAddress: {i[4]}\n")
            else:
                search_output.insert(tk.END,"Sorry,no such entry is found!\n")
search_button = tk.Button(root, text="Search",bg="yellow2", command=search_contact)
search_button.grid(row=7, column=1,pady = 5)
address1_label = tk.Label(root, text="Created by Piyush Gupta",font = ("Segoe Script",8),bg = "lawn green",fg = 'red')
address1_label.grid(row=20, column=0,pady = 5,columnspan = 2)

root.mainloop()