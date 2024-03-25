from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import sqlite3    

root = Tk()
root.title('Codemy.com - Lear To Code!')
root.geometry("500x400")


'''
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
)
        """)
'''
def submit():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
            })
    conn.commit()
    conn.close()
    
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    
    
def query():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()
    
    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    
    print_records = ""
    for record in records:
        print_records += "ID: " + str(record[6]) + " \tName: " + str(record[0]) + " " + str(record[1]) + " \tAddress: " + str(record[2]) + " \tCity: " + str(record[3]) + " \tState: " + str(record[4]) + " \tZipcode: " + str(record[5]) + "\n"
        
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)
    conn.commit()
    conn.close()  
    
    
def update():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()
    
    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET 
                first_name = :f_name,
                last_name =  :l_name, 
                address = :address, 
                city = :city, 
                state = :state, 
                zipcode = :zipcode
                
                WHERE oid = :oid""",
              {
                  'oid': record_id,
                  'f_name': f_name_editor.get(),
                  'l_name': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get()
            })
    
    
    conn.commit()
    conn.close() 
    
    editor.destroy()
    

def edit():
    global editor
    editor = Tk()
    editor.title('Codemy.com - Lear To Code!')
    editor.geometry("500x400")

    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    record_id = delete_box.get()
    print(f"{record_id = }")
    
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)
    
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, padx=20, pady=(10, 0))
    
    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)
    
    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)
    
    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)
    
    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)
    
    zipcode_label_editor = Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=5, column=0)
    
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
    
    submitButton_editor = Button(editor, text="Save Recoord", command=update)
    submitButton_editor.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137 ) 


def delete():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()
    c.execute("DELETE FROM addresses WHERE oid=" + delete_box.get())    
    
    conn.commit()
    conn.close()  

      
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=0)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, padx=20, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_label = Label(root, text="ID Number")
delete_label.grid(row=9, column=1)

submitButton = Button(root, text="Add Record To Database", command=submit)
submitButton.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

queryButton = Button(root, text="Show Records", command=query)
queryButton.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

deleteButton = Button(root, text="Delete Records", command=delete)
deleteButton.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

editButton = Button(root, text="Edit Records", command=edit)
editButton.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

root.mainloop()