from tkinter import *
from PIL import ImageTk,Image
    
root = Tk()
root.title("Codemy.com Image Viewer")

r = IntVar()
r.set("2")

def clicked(value):
    myLabel = Label(root,text=value)
    myLabel.pack()

Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 3", variable=r, value=3, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 4", variable=r, value=4, command=lambda: clicked(r.get())).pack()

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")    
    ]

pizza = StringVar()
pizza.set("Pepperoni")

myLabel = Label(root, text=r.get())
myLabel.pack()

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

pizzaLabel = Label(root, text=pizza.get())
pizzaLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(r.get()))
myButton.pack()
root.mainloop()