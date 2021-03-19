

class SoftwareEngineer:
    def __init__(self):
        self._salary = None
    
#=======This is more python way to use getter and setter ================    
    #getter
    @property
    def salary(self): # take off get_salary
        return self._salary    
        
    #setter 
    @salary.setter
    def salary(self, value):
        self._salary = value
        
    @salary.deleter
    def salary(self):
        del self._salary
    
    
se = SoftwareEngineer()





se.salary = 60020
print(se.salary)

del se.salary
print(se.salary)