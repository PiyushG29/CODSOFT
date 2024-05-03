from tkinter import *
from tkinter import messagebox

tasks_list = []
counter = 1

def clear_taskNumberField():
    taskNumberField.delete(0.0, END)

def clear_taskField():
    enterTaskField.delete(0, END)

def insertTask():
    global counter
    value = inputError()
    if value == 0 :
        return

    content = enterTaskField.get() + "\n"
    tasks_list.append(content)
    TextArea.insert('end -1 chars', "{" + str(counter) + "} " + content)
    
    counter += 1 
    clear_taskField()

def inputError():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error")
        return 0
    return 1

def updateTask():
    global tasks_list

    value = inputError()
    if value == 0:
        return
  
    number = taskNumberField.get(1.0, END)
    new_content = enterTaskField.get() + "\n"
  
    if number == "\n":
        messagebox.showerror("Input Error", "Please enter a valid task number.")
        return
    try:
        task_no = int(number) - 1 
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer for task number.")
        return

    if task_no < 0 or task_no >= len(tasks_list):
        messagebox.showerror("Error", "Invalid task number. Please enter a number between 1 and {}".format(len(tasks_list)))
        return

    tasks_list[task_no] = new_content
   
    clear_taskNumberField()
    clear_taskField()
  
    TextArea.delete(1.0, END)
    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars', "{" + str(i + 1) + "}" + tasks_list[i])


def delete():
    global counter
     
    if len(tasks_list) == 0 :
        messagebox.showerror("No task")
        return
 
    number = taskNumberField.get(1.0, END)

    if number == "\n" :
        messagebox.showerror("input error")
        return
     
    else :
        task_no = int(number)
 
    clear_taskNumberField()
    tasks_list.pop(task_no - 1)
    counter -= 1
    TextArea.delete(1.0, END)
 
    for i in range(len(tasks_list)) :
        TextArea.insert('end -1 chars', "{}" + str(i + 1) + "} " + tasks_list[i])

# Driver code
if __name__ == "__main__":
    gui = Tk()

    gui.configure(background = "sienna3")

    gui.title("To-Do List")
    gui.geometry("250x450")
    
    enterTask = Label(gui, text = "Enter Your Task", font = ('Helvetica',14),bg = "magenta2")

    enterTaskField = Entry(gui)

    Submit = Button(gui, text = "Submit", fg = "Black", bg = "lawn green", command = insertTask)
    TextArea = Text(gui, height = 5, width = 25, font = "lucida 13")

    task_1 = Label(gui, text = "Delete / Update Task Number", font = ('Segoe Script',10),bg = "dodger blue")                      
    taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13")
    update = Button(gui, text="Update", font = ('@GungsuhChe',10),fg="Black", bg="Yellow", command=updateTask)
    delete = Button(gui, text = "Delete",font = ('@Kozuka Gothic Pr6N EL',10), fg = "Black", bg = "Red", command = delete)
    enterTask.grid(row = 0, column = 2,pady = 4)
    
 
    enterTaskField.grid(row = 1, column = 2, ipadx = 50)                    
    Submit.grid(row = 2, column = 2,pady = 15)
    TextArea.grid(row = 3, column = 2, padx = 10,pady = 20, sticky = W)                    
    task_1.grid(row = 4, column = 2, pady = 5)                     
    taskNumberField.grid(row = 5, column = 2)                  
    delete.grid(row = 6, column = 2, pady = 5)  
    update.grid(row=7, column=2,pady = 18)
    task_2 = Label(gui, text = "Created by Piyush Gupta", font = ('Segoe Script',8),bg = "lawn green",fg = "red")
    task_2.grid(row = 9,column = 2, pady = 5)
    gui.mainloop()