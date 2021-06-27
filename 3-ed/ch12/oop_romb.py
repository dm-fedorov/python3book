# oop_romb.py
class Person:
    def hello(self):
        print("I am Person")
    
class Student(Person):
    def hello(self):
        print("I am Student")
        
class Prof(Person):
    def hello(self):
        print("I am Prof")

# Множественное наследование от двух классов:
class Someone(Student, Prof):
    pass
