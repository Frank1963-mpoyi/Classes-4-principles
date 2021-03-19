

class SoftwareEngeneer:
    
    # class attribute
    alias = "Keyboard"
    
    
    def __init__(self, position, name, age, level, salary): 
        
        # instance attribute
        self.position   =   position
        self.name       =   name
        self.age        =   age
        self.level      =   level
        self.salary     =   salary
    
    # instance methode 
    def code(self): # we have to put self in instance method in order to access all the instance attribute
        print(f"{self.name} is writing code....")
    
    # this method we can only use it with class not instances because there is not self  
    def entry_salary(age):
        if age < 25:
            return 5000
        elif age < 30:
            return 700
        return 75000
    
    @staticmethod
    def entry_salary1(age):
        #if self.age < 25: we can not access the instance attribute
        if age < 25:
            return 8000
        elif age < 30:
            return 6900
        return 75000
    
sof1 = SoftwareEngeneer("software Engineer", "Frank Tshibuyi", 20, "mid level", 5000) # the self is pass automaticaly in like first argument
sof2 = SoftwareEngeneer("software Engineer", "Frank Tshibuyi", 20, "mid level", 5000)

print(SoftwareEngeneer.entry_salary(25))# it only work with class not instances because there is not self

#=======With Decorator it will start to work with class and instances  but we can not access the instance attribute===============
print(sof1.entry_salary1(30))