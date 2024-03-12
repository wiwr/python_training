'''
Created on Mar 6, 2024

@author: witek
'''
class Person:
    def __init__(self,name):
        self.name = name
        
        
    def get_name(self):
        return self.__name
    
    
    def set_name(self,value):
        self.__name = value
    
        
class Student(Person):
    def __init__(self, student_id, student_marks):
        self.__student_id = student_id
        self.student_marks = student_marks
    
        
    def get_student_id(self):
        return self.__student_id
    
    
    def get_student_marks(self):
        return self.student_marks
    
    
    def set_student_id(self,value):
        self.__student_id = value
    
        
    def set_student_marks(self,value):
        self.student_marks = value
    
        
class SomeClass:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.__num2 = num2
    
    
    def get_num1(self):
        return self.num1
    
    
    def get_num2(self):
        return self.__num2
    
    
    def set_num1(self,value):
        self.num1 = value
    
        
    def set_num2(self,value):
        self.__num2 = value
    
        
    def validate(self):
        return("num1 and num2 are equal", self.get_num2() == self.get_num1())  
    
    
class Child(SomeClass):
    pass      
    
if __name__ == "__main__":
    student = Student(909090,77)
    student.set_name("Jack")
    print(student.get_name(),student.get_student_id(),student.get_student_marks())
    print(Student.__name__)
    print(Student.__module__)
    print(Student.__bases__)
    
    child = Child(100,100)
    print(child.validate())
    print(isinstance(child, Child))  