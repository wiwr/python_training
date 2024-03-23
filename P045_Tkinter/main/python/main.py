from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
    

root = Tk()
root.title("Codemy.com")
root.geometry("400x400")

var = StringVar()


def show():
    myLabel = Label(root, text=var.get()).pack()

checkButton = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="ON", offvalue="OFF")
checkButton.deselect()
checkButton.pack()


myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()