# Inheritance is the  process of one class take the attribute and the 
# method of another class
# its Parent and Child class



# inherit, extend, override
class Employee:
    
    def __init__(self, name, age):
        self.name   = name
        self.age    = age
        
    def walk(self):
        print(f"{self.name} is walking .......")

class SoftwareEngineer(Employee):
    pass

class Designer(Employee):
    pass


# Note: instead of SoftwareEngineer an Employee has name and surname it can inherit from parent class Employee same as Design

student = SoftwareEngineer('Frank', 39)
student.walk()
print(f"this is the record of the Student : {student.name} and has {student.age} years old")

# it will inherit both attribute instances and method instances
student1 = Designer('Ruth', 38)
student1.walk()
print(f"this is the record of the Student : {student1.name} and has {student1.age} years old")