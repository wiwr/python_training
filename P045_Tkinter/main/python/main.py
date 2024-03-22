from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

    
root = Tk()
root.title("Codemy.com Image Viewer")


def info():
    messagebox.showinfo("This is my Popup!", "Hello Info Popups!")


def warning():
    messagebox.showwarning("This is my Popup!", "Hello Warning Popups!")
    
    
def error():
    messagebox.showerror("This is my Popup!", "Hello Error Popups!")
    
    
def askquestion():
    response = messagebox.askquestion("This is my Popup!", "Hello AskQuestion Popups!")
    Label(root, text=response).pack()
    
def askokcancel():
    response = messagebox.askokcancel("This is my Popup!", "Hello AskOkCancel Popups!")
    Label(root, text=response).pack()
    
def askyesno():
    response = messagebox.askyesno("This is my Popup!", "Hello AskYesNo Popups!")
    Label(root, text=response).pack()
                    
Button(root, text="Popup - showinfo", command=info).pack()
Button(root, text="Popup - showwarning", command=warning).pack()
Button(root, text="Popup - showerror", command=error).pack()
Button(root, text="Popup - askquestion", command=askquestion).pack()
Button(root, text="Popup - askokcancel", command=askokcancel).pack()
Button(root, text="Popup - askyesno", command=askyesno).pack()

root.mainloop()