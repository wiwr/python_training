from tkinter import *
from PIL import ImageTk,Image
    
root = Tk()
root.title("Codemy.com Image Viewer")

frame = LabelFrame(root, text="This is my Frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)

button1 = Button(frame, text="Don't Click Here!")
button2 = Button(frame, text="...or here!")
button1.grid(row=0, column=0)
button2.grid(row=1, column=1)

root.mainloop()