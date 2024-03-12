'''
Created on Mar 6, 2024

@author: witek
'''
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

    
class Dog(Animal):
    def speak(self):
        return "Woof!"

    
class Cat(Animal):
    def speak(self):
        return "Meow!"

    
class Cow(Animal):
    def speak(self):
        return "Moo!"

    
def make_animal_speak(animal):
    print(animal.speak())

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    cow = Cow()
    
    make_animal_speak(dog)
    make_animal_speak(cat)
    make_animal_speak(cow)