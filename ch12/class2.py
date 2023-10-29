# class2.py
class Person:
    def __init__(self, name='Человек без имени'):
        self.name = name
        self.age = 0
    def say(self):
        print("{0} говорит".format(self.name))

class Employee(Person):
    def __init__(self, name):
        Person.__init__(self)
        self.job_title = 'Безработный'
    def set_job(self, job_title='Безработный'):
        self.job_title = job_title        
    def get_job(self):
        print(self.name, self.job_title)
    
class Customer(Person):
    def __init__(self, name):
        Person.__init__(self)
        self.email = 'Нет почты'
    def set_email(self, email='Нет почты'):
        self.email = email        
    def get_email(self):
        print(self.name, self.email)

person = Person('Иван')
person.say()

emp = Employee('Игорь')
emp.say()
emp.get_job()

cust = Customer('Петр')
cust.say()
cust.get_email()
