from tkinter import *
from tkinter import Menu
from tkinter import messagebox

#def clicked():
   #a = new_window()

def save():
    messagebox.showinfo("Save file", 'Saved')


def openNewWindow():
    #newWindow = Toplevel(window)
    #newWindow.title("New Window")
    #newWindow.geometry("500x300")
    #Label(newWindow, text="This is new window").pack()

    newWindow = Tk()
    newWindow.title("Welcome to new window")
    menuNew = Menu(newWindow)
    new_item = Menu(menuNew, tearoff=0)
    new_item.add_command(label='New', command=openNewWindow)
    new_item.add_command(label='Open')
    new_item.add_separator()
    new_item.add_command(label='Save', command=save)
    new_item.add_command(label='Save As')
    menuNew.add_cascade(label='File', menu=new_item)

    new_item = Menu(menuNew)
    new_item.add_command(label='Undo')
    menuNew.add_cascade(label='Edit', menu=new_item)
    window.config(menu=menuNew)




#def clicked():
    #window1=open()

window = Tk()
window.title("Welcome to Dashboard")
menu = Menu(window)
new_item = Menu(menu, tearoff=0)    #mathi ko --- line hataune tearoff=0
new_item.add_command(label='New', command=openNewWindow)
new_item.add_command(label='Open')
new_item.add_separator()
new_item.add_command(label='Save', command=save)
new_item.add_command(label='Save As')
menu.add_cascade(label='File', menu=new_item)

new_item = Menu(menu)
new_item.add_command(label='Undo')
menu.add_cascade(label='Edit', menu=new_item)
window.config(menu=menu)
window.mainloop()