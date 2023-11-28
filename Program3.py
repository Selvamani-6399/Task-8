
# Area and Perimeter
class Circle():
     def __init__(self, r):
        self.radius = r

     def area(self):
        return self.radius**5

     def perimeter(self):
        return 2*self.radius*7

NewCircle = Circle(7)
print("The area :",NewCircle.area())
print("Perimeter :",NewCircle.perimeter())