

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
    def entry_salary1(age):
        if age < 25:
            return 5000
        elif age < 30:
            return 700
        return 75000
    
    
    def entry_salary(self, age):
        if age < 25:
            return 5000
        elif age < 30:
            return 700
        return 9000
    
    
    #dunder method
    # special method will execute if our object is convert to a string
    # we want to have information when we print our object
    def __str__(self):
        information = f"name : {self.name} and the age: {self.age}"
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age== other.age



sof1 = SoftwareEngeneer("software Engineer", "Frank Tshibuyi", 20, "mid level", 5000) # the self is pass automaticaly in like first argument
sof2 = SoftwareEngeneer("software Engineer", "Frank Tshibuyi", 20, "mid level", 5000)

print(sof1)# before it was printing this : <__main__.SoftwareEngeneer object at 0x01297298>
# now with the presence of the de __str__(self), we can get information about our object


'''
Default: its provide class name object at memory location 0x01297298

print(sof1)
<__main__.SoftwareEngeneer object at 0x01297298> , 
class name object at memory location 0x01297298

this dont tell us a lot thing  about our object 

'''

# we want to have information when we print our object
# def __str__(self):
#         return info


print(sof1 == sof2)# the result is false but the have the same data but they dont have the same memory location
# false because it comparing memoring address
# def __eq__(self): by Deault gives false 


# def __eq__(self, other):
#     return self.name == other.name and self.age== other.age
# it will give True like overide the default 

print(sof1.entry_salary(20))

print(SoftwareEngeneer.entry_salary1(54))