# OBJECT ORIENTED PROGRAMMING
# Object Oriented Programming is a programming approach where we organize codes using objects.

# CLASS AND OBJECT
#=============================================================
# A class is similar to a blueprint or template.
# An object, on the other hand, is the actual item created from that class.
# For example, if you have a Car CLASS, it contains various OBJECTS such as
# Engine Number, Model, Design, Brand; per se:

'''
Public Class Car:
    engineNumber()
    model()
    design()
    brand()
'''

# EXAMPLE 1
#=============================================================
'''
class Student:
    def __init__(self, name, course, year_level):
        self.name = name
        self.course = course
        self.year_level = year_level

    def display_Info(self):
        print(f"Student Name: {self.name}")
        print(f"Student Course: {self.course}")
        print(f"Student Year Level: {self.year_level}")

student1 = Student("Nicki Minaj", "CompTech", 2)
student1.display_Info()
'''

# INIT AND SELF METHOD
#=============================================================
# The __init__() method is called automatically when an object is created.
# It is commonly used to initialize all particular attributes of an object
# pertaining to a class.

# The keyword SELF refers to the current object.
# It allows the class to access its own attributes and methods.

'''
FOUR MAIN PRINCIPLES OF OOP
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
'''

# Encapsulation | Keeping the data and methods within the class. It also helps to protect the data from being directly changed.
#==============================================================================================================================

'''
class BankAccount():
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        # The double underscore protects the data inside the
        # balance variable being encapsulated

    def show_balance(self):
        print("Owner Name:", self.owner_name)
        print("Balance:", self.__balance)

account_ni_feli = BankAccount("Felicity Batumbakal", 10000)
account_ni_feli.deposit(5000)
account_ni_feli.show_balance()
'''

# Inheritance | It allows once class to reuse the attributes and methods of another class.
#==============================================================================================================================

'''
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Teacher(Person):
    def teach(self):
        print(f"Mr. {self.name} is a teacher in TUPV.")

teacher1 = Teacher("Joseph Octavino", 30)
teacher1.introduce()
teacher1.teach()
'''

# Polymorphism | Having the same method name but different behavior depending on the object.
#==============================================================================================================================

'''
class Dog():
    def sound(self):
        print(f"Dog is Barking.")

class Cat():
    def sound(self):
        print(f"Cat is Meowing.")

dog = Dog()
dog.sound()
cat = Cat()
cat.sound()
'''

# Abstraction | Hiding unnecessary details and showing only the important features.
#==============================================================================================================================

'''
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class GCashPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using GCash.")

payment = GCashPayment()
payment.pay(100)
'''