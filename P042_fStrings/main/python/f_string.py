'''
Created on Mar 11, 2024

@author: witek
'''
from datetime import datetime

class Hello:
    def __init__(self, message):
        self.message = message
    
    
    def __format__(self, format_spec):
        if format_spec == 'u':
            return self.message.upper()
        elif format_spec == 'l':
            return self.message.lower()
        return self.message
        

if __name__ == "__main__":
    name = "Jan Kowalski"
    
    hello = Hello(name)
    print(f'{hello:l}')
    print(f'{hello:u}')
    
    print(f'Hello {name.upper()=}')
    
    books = [
            {"title":"Białe noce", "author":"Addm Przechrzta", "pages":250},
            {"title":"Wilczy Legion", "author":"Addm Przechrzta", "pages":350},
            {"title":"Gambit Wielkopolskiego", "author":"Addm Przechrzta", "pages":-100}    
    ]
    
    dashNum = 46
    print("-"*dashNum)
    print(f'{"Title":30} {"Author":20}')
    for book in books:
        print(f'{book["title"]:30} {book["author"]:20}')
    
    print("-"*dashNum)
    print(f'{"Title":^20} {"Author":^20}')
    for book in books:
        print(f'{book["title"]:>20.20} {book["author"]:20}')
    
    print("-"*dashNum) 
    width = '20'   
    print(f'{"Title":^{width}} {"Author":^{width}}')
    for book in books:
        print(f'{book["title"]:>{width}.{width}} {book["author"]:{width}}')
    
    print("-"*dashNum) 
    width = '20'   
    print(f'{"Title":^{width}} {"Author":^{width}}')
    for book in books:
        print(f'{book["title"]:>{width}.{width}} {book["pages"]:> 10} {book["pages"]:=+010}')
    
    num = 293949
    print("-"*dashNum)
    print(f'{num:o}')
    print(f'{num:x}')
    print(f'{num:d}')
    print(f'{num:n}')
    print(f'{num:c}')
    print("-"*dashNum)
    print(f'{num:b}')
    print(f'{num:#b}')
    print(f'{num:#_b}')
    print("-"*dashNum)
    
    
    big_number: int = 1_620_000_000
    print(f'{big_number:e}')
    print(f'{big_number:.2e}')
    
    now: datetime = datetime.now()
    date_space: str = '%Y-%m-%d'
    print(f'{now=:{date_space}}')
    
    number: float = 1000000.1234567
    spec: str = ',.2f'
    print(f'{number:{spec}}')
    
    custom_folder: str = "Indetly"
    path: str = r'\Users\federico\Documents\folder'
    print(path)
    path: str = fr'\Users\federico\Documents\{custom_folder}'
    print(path)
    
    a: float = 0.1
    b: float = 0.2
    print(f'{a + b = }')
    print(f'{a + b = :.1f}')
    
    name: str = 'Bob'
    print(f'{name = }')
    
    
    print(f'{name = !s}')
    print(f'{name = !a}')
    print(f'{name = !r}')