# abstraction is like extention of encapsulation
# each object can only expose high mechanism for using it this mechanism can hide the internal implementations detail 
# and only reveal the operation relevant for the other object


class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        self._salary = None
        self._num_bugs_solved = 0
        
    
    
    def code(self):
        self._num_bugs_solved += 1   
    
    
    def get_salary(self):
        return self._salary    
        
        
    def set_salary(self, base_value):
        
        self._salary = self._calculate_salary(base_value)
        
    
    
    # Abstraction dont care about the internal implementation to calculate salary
    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3
    
    
    
se = SoftwareEngineer("Frank", 39)


for i in range(70): 
    print(f"the code is {se.code()}")
    


# This is Abstraction only care about the oucome not the internaly implementation    
se.set_salary(6000)
print(se.get_salary())