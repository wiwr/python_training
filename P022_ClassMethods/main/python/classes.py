'''
Created on Mar 6, 2024

@author: witek
'''
class Student:
    def __init__(self, student_id, student_name, student_marks):
        self.student_id = student_id
        self.student_name = student_name
        self.__student_marks=student_marks
        
        
    def get_student_id(self):
        return self.__student_id
    
    
    def get_student_name(self):
        return self.__student_name
    
    
    def get_student_marks(self):
        return self.__student_marks
    
    
    def set_student_id(self,value):
        self.__student_id = value
    
    
    def set_student_name(self, value):
        self.__student_name = value
    
    
    def set_student_marks(self,value):
        self.__student_marks = value
    
        
    def validate_marks(self):
        if self.get_student_marks() >= 70:
            return "Passed"
        return "Not Passed"
    
    
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
    
    
if __name__ == "__main__":    
    student = Student(500, "John Jones", 77)
    print(student.student_id)
    print(student.student_name)
    print(student.__dict__)
    print(student.validate_marks())
    
    someClass = SomeClass(50,60)
    someClass.set_num1(200)
    someClass.set_num2(100)
    print(someClass.get_num1())
    print(someClass.get_num2())
    print(someClass.validate())
    print(hasattr(someClass,"_SomeClass__num2"))
    print(SomeClass.__name__,SomeClass.__module__,SomeClass.__bases__)  