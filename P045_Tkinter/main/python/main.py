from tkinter import *

root = Tk()
root.title("Learn To Code at Codemy.com")

#root.iconbitmap('ico.ico')

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()