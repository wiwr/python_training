class Student:
    def __init__(self, student_id,student_name,student_marks):
        self.student_id = student_id
        self.student_name = student_name
        self.__student_marks = student_marks
        
class SomeClass:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.__num2 = num2
        
    def some_method(self):
        pass        
        
student = Student(500, "John Jones",77)
print(student.student_id)
print(student.student_name)
print(student.__dict__)

someClass = SomeClass(50,60)
print(someClass.__dict__)
print(dir(someClass))
print(someClass._SomeClass__num2)
print(someClass.__dict__)
someClass.__dict__["_SomeClass__num2"]=100
someClass.__dict__["num5"]=100
print(someClass.num5)
print(someClass._SomeClass__num2)
print(someClass.__dict__)
print(someClass.num5)
print("anotherClass")
anotherClass = SomeClass(50,60)
try:
    print(anotherClass.num5)
except AttributeError as e:
    print("add num5")
    anotherClass.__dict__["num5"] =700
print(anotherClass.num5)