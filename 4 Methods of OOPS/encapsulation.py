
# Encapsulation is an Object Oriented Programming concept that binds together the data and functions that manipulate the data, 
# and that keeps both safe from outside interference and misuse. 
# The best example of encapsulation could be a calculator. 


# Encapsulation is a mechanisme of hiding data implementations
# means that instances variables are kept private there is onlyone access method for outside which we can access and change method call getter() and setter() method

# instance method can be also kept private and use internally only not from the outside


class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name # this is external use
        self.age = age # this is external use
        #self.__salary = None private with double underscore
        self._salary = None # this is private internally use only
        self._num_bugs_solved = 0 #this is private internally use only
        
        #note: _salary: is called a "protected" attribute(one underscore)
        # __salary: is called a "private" attribute (double underscore)
        
        # Here i use the word "private" for internal attributes with only one leading underscore as well
    
    # they implement this in order to get a value for _num_bugs_solved 
    def code(self):
        self._num_bugs_solved += 1   # with += 1 we need for loop to implemet by 1 until we reach 70 
    
    # public function is the only way the outside can access the protected attribute
    #getter
    def get_salary(self):
        return self._salary    
        
    # public function is the only way the outside can access the protected attribute
    #setter    
    def set_salary(self, base_value):
        
        self._salary = self._calculate_salary(base_value)
        
    
    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3
    
    
    
se = SoftwareEngineer("Frank", 39)
# print(se.age, se.name, se._salary )


for i in range(70): # 
    print(f"the code is {se.code()}")
    
    
se.set_salary(6000)
print(se.get_salary())