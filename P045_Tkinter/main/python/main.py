from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
    

root = Tk()
root.title("Codemy.com")
root.geometry("400x400")

options = ["Monday", 
           "Tuesday", 
           "Wednesday", 
           "Thursday", 
           "Friday"
           ]

def show():
    myLabel = Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()