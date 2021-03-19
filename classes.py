# position, name, age, level, salary
set1 = ["software Engineer", "Frank", 20, "mid level", 5000]
set2 = ["software Engineer", "Mpoyi", 39, "Senior", 7000]



class SoftwareEngeneer:
    
    # this is class attribute
    alias = "Keyboard" # you can access class attribute in every instance of class and class itself
    
    def __init__(self, position, name, age, level, salary): # __init__() its a specia; method to initialise our object
        # instance attribute 
        self.position   =   position
        self.name       =   name
        self.age        =   age
        self.level      =   level
        self.salary     =   salary
        #self.position #is instance attribute = position # is outside parameter refer in the __init__() method
        # instance attribute is only tiet to only one instance or one object
        
        


sof1 = SoftwareEngeneer("software Engineer", "Frank", 20, "mid level", 5000) # the argument we pass refer to outside parameter
sof2 = SoftwareEngeneer("software Engineer", "Mpoyi", 39, "Senior", 7000)


print(f"The Company Portofolio is : {sof1.position} name: {sof1.name}")
print(f"The Company Portofolio is : {sof2.position} name: {sof2.name}")
#(.) dot allow us to access instance attribiute 
# eg : soft1.name 



#print(sof1)
#<__main__.SoftwareEngeneer object at 0x00C57178>

'''
the different between instance  attribute and class attribute is 
instance attribute belong only to one object created like sof1 not sof2

you can access class attribute in every instances like in sof1 and sof2
print(sof1.alias)
print(sof2.alias)
'''


'''
Exemple : 

#print(SoftwareEngeneer.name) # it doesnt work because name is attached to a specific instance
print(SoftwareEngeneer.alias)
'''
# print(sof1.alias)
# print(sof2.alias)