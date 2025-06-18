'''
import day3 #creating custom modules
day3.greet("Cossa")

day3.add(5,6)
'''
#OOP IN PYTHON -> CLASS AND OBJECT
class student:
    def __init__(self,name,roll_number,age):
        self.name=name
        self.roll_number=roll_number
        self.age=age
    def greet(self):
        print("Welcome ",self.name)
    def details(self):
        print(f"Roll number ={self.roll_number}, age ={self.age}")

ian=student("ian","87","20")
ian.greet()
ian.details()

class Car:
    def __init__(self,model,year):
        self.model=model
        self.year=year

mycar=Car("Tesla",2023)
print(mycar.model,mycar.year) 

class laptop(student):
    def __init__(self, name, roll_number, age, company,model_no,ram ):
        super().__init__(name, roll_number, age)
        self.company=company
        self.model_no=model_no
        self.ram=ram
    def printspec(self):
        print(f"{self.name}your model spec= company:{self.company},model:={self.model_no},ram={self.ram}")

andile=laptop("Andile",65,24,"cyborg15","MSI Cyborg 15 A12",32)
print(andile.name,andile.age,andile.roll_number,andile.company,andile.model_no,andile.ram)



'''
OOPS Features:
class and objects
inheritance -> reusability
Encapsulation -> Data is binded with code
Polymorphism -> Many forms-> code(Same code acting in different forms)many methods
Runtime Polymorphism & Compile-time polymorphism
'''
class Bird:
    def sound(self):
        print("Chirp")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()
b = Bird()
c= Cat()

make_sound(b)
make_sound(c)
#run-time polymorphism
class Parent:
    def show(self):
        print("Parent's method")
class Child(Parent):
    def show(self):
        print("Child's method")

obj= Child()#creating obj object in Child's class
obj.show()

#Compile-time polymorphism
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):#overloading a operator 
        return Point(self.x+other.x,self.y+other.y)
p1= Point(1,2)
p2= Point(3,4)
p3 = p1+p2
print(p3.x,p3.y)