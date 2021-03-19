
# inherit, extend, override
class Employee:
    
    def __init__(self, name, age, salary):
        self.name   = name
        self.age    = age
        self.salary = salary
        
    def walk(self):
        print(f"{self.name} is walking .......")



# we extend Here
class SoftwareEngineer(Employee):
    # we want also this child class to have it own attribute and method
    
    def __init__(self, name, age, salary, level):
        # we dont do self.name = name //instead we call the __init__() for the parent class with key word super()
        super().__init__(name, age, salary) # now the parent class is initialize correctly
        self.level = level # this level only work for SoftwareEngineer not for Employee class and Designer class
    
    
    def debug(self):
        print(f"{self.name} is debugging .......")



class Designer(Employee):
    
    # this is only specific to the child class
    def draw(self):
        print(f"{self.name} is drawing .......")






# Note: instead of SoftwareEngineer an Employee has name and surname it can inherit from parent class Employee same as Design

student = SoftwareEngineer('Frank', 39, 6000, "Junior")
student.debug()
print(f"this is the record of the Student : {student.name} and has {student.age} years old and his salary is {student.salary} position is {student.level}")


# it will inherit both attribute instances and method instances
student1 = Designer('Ruth', 38, 7500)
student1.draw()
print(f"this is the record of the Student : {student1.name} and has {student1.age} years old and salary is {student.salary}")