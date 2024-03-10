'''
Created on Mar 10, 2024

@author: witek
'''
from dataclasses import dataclass, field

@dataclass(order=True) #, frozen=True)
class Book:
    sort_index: int = field(init=False, repr=False)
    title: str
    author: str
    pages: int 
    isbn: str
    id: int = 100
    
    def __post_init__(self):
        #self.sort_index = self.pages
        object.__setattr__(self,'sort_index',self.id)
        
    def __str__(self):
        return f'-------BOOK-------\nTitle: "{self.title}"\nAuthor: {self.author}\nISBN: {self.isbn}\nPages: {self.pages}\n------------------'    
    # def __init__(self, title, author, pages, isbn):
    #     self.title = title
    #     self.author = author
    #     self.pages = int(pages)
    #     self.isbn = isbn
        
book1 = Book("Dziennik Cwaniaczka", "Jeff Kinney", 200, "978-83-10-13950-4")
book2 = Book("Opowieść wigilijna", "Chales Dickens", 119, "978-83-7399-310-5")
book3 = Book("Wędrowcy", "Joanna Papuzińska", 94, "978-83-7672-090-6")
book4 = Book("Wędrowcy", "Joanna Papuzińska", 94, "978-83-7672-090-6")

books = [book1, book2, book3, book4]

for book in books:
    print(book)


print(book3 == book4)
print(book1 == book2)