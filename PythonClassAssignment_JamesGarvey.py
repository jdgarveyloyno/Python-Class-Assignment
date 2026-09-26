class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def setWidth(self, w):
        self.width = w
        
    def setHeight(self, h):
        self.height = h
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width * 2) + (self.height * 2)
    

def area_difference(rect1, rect2):
    return rect1.area() - rect2.area()

r = Rectangle(5, 4)  # width 5 and height 4
area = r.area()
perimeter = r.perimeter()

print("width:", r.getWidth(), " height:", r.getHeight())
print("area:", r.area(), " perimeter:", r.perimeter())
        
r.setWidth(10)
r.setHeight(15)
print("Set new width and height")
area = r.area()
perimeter = r.perimeter()
print("width:", r.getWidth(), " height:", r.getHeight())
print("area:", r.area(), " perimeter:", r.perimeter())

r1 = Rectangle(10, 10)
r2 = Rectangle(15, 20)
diff = area_difference(r1, r2)
print("area of r1:", r1.area(), " area of r2:", r2.area())
print("area difference:", diff)
