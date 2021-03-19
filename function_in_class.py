set1 = ["software Engineer", "Frank", 20, "mid level", 5000]
set2 = ["software Engineer", "Mpoyi", 39, "Senior", 7000]

def code(se):
    print(f"{se[1]} is writing code....")

code(set1)

# the example above will work but it will better if we tiet our data and function in the class
#=====================================================================================


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
        
    def code_in_language(self, language): # we can also use parameter in instance function
        print(f"{self.name} is writing code in {language}....")


    # we can also return things
    def info(self):
        information = f"name : {self.name} and the age: {self.age}"
        return information




sof1 = SoftwareEngeneer("software Engineer", "Frank Tshibuyi", 20, "mid level", 5000) # the self is pass automaticaly in like first argument
sof2 = SoftwareEngeneer("software Engineer", "Mpoyi Wa Tshibuyi", 39, "Senior", 7000)


# now this instance can do something 
print(sof1.code()) # self method is passed automatically in the function
print(sof2.code())
sof1.code_in_language("Python")# we can also use argument in instance function

print(sof1.info())