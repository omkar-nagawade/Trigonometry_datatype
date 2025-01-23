import math

class Trigonometry:
    def __init__(self, value):
        self.value = value
    
    def sin(self):
        return math.sin(math.radians(self.value))
    
    def cos(self):
        return math.cos(math.radians(self.value))
    
    def tan(self):
        return math.tan(math.radians(self.value))
    
    def cot(self):
        return 1 / math.tan(math.radians(self.value))
    
    def sec(self):
        return 1 / math.cos(math.radians(self.value))
    
    def csc(self):
        return 1 / math.sin(math.radians(self.value))
    
    def __str__(self):
        return f"Trigonometry({self.value} degrees)"


angle1=Trigonometry(90)
print(angle1.sin())