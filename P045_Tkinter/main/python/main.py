from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

def slide(hor):
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()) )
    

root = Tk()
root.title("Codemy.com")
root.geometry("400x400")

vertical = Scale(root, from_=100, to=700)
vertical.pack()

horizontal = Scale(root, from_=100, to=700, orient=HORIZONTAL, command=slide)
horizontal.pack()


my_button = Button(root, text="Click Me!!", command=slide).pack()

root.mainloop()