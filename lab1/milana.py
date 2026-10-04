class Rectangle:
    def _init_(self, length, width):
        self.length=length
        self.width=width
        
    def area(self,length,width):
        return length*width
    
    def perimetr(self):
    
        return 2*(self.length+self.width)
    
    
a=int(input())
b=int(input())  
rectangle = Rectangle(a, b)

print(rectangle.area())
print(rectangle.perimetr())