#Calculator mileko chaina

from tkinter import *
from tkinter import messagebox

def clicked():
    numone= int(txtnum1.get())
    numtwo= int(txtnum2.get())
    sum = numone + numtwo
    lbl.configure(text="The sum is ", sum)
    #messagebox.showinfo('The sum is : ', sum)

    lbl.configure(text=res)

window = Tk()


#textbox
num1 = Label(window, text="Num 1:", font=("Arial ", 10))
num1.grid(column=0, row=5)
txtnum1 = Entry(window, width=10)
txtnum1.grid(column=1, row=5)
num2 = Label(window, text="Num 2:", font=("Arial ", 10))
num2.grid(column=0, row=6)
txtnum2 = Entry(window, width=10)
txtnum2.grid(column=1, row=6)
btn = Button(window, text="Sum", bg="orange", fg="red", command=clicked)
btn.grid(column=7,row=7)

window.mainloop()