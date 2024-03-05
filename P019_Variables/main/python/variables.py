'''
Created on Mar 5, 2024

@author: witek
'''
class MyClass:
    def __init__(self):
        #Public variable
        self.public_var = 10
        #Private variable
        self.__private_var = 20
    
    def get_private_var(self):
        return self.__private_var
    
    def set_private_var(self, value):
        self.__private_var = value
        
obj = MyClass()

print("Public variable:", obj.public_var)
print("Private variable (using getter):",obj.get_private_var())
try:
    print("Private variable (direct access):",obj.__private_var)
except AttributeError as e:
    print(e) 
obj.set_private_var(30)
print("Private variable (after modification):",obj.get_private_var())