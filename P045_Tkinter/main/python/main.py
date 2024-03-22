from tkinter import *
from PIL import ImageTk,Image


def open():
    global my_img
    top = Toplevel()
    top.title("Second")
    label = Label(top, text="Hello World").pack()
    my_img = ImageTk.PhotoImage(Image.open("images/hot.png"))
    my_label = Label(top, image=my_img).pack()
    buttonC = Button(top, text="Close window", command=top.destroy).pack()
    
root = Tk()
root.title("Codemy.com Image Viewer")

button = Button(root, text="Open Second Window", command=open).pack()

root.mainloop()