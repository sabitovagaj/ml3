class Figure:
   def __init__(self, color):
       self.color = color

   def get_color(self):
       return self.color


class Rectangle(Figure):
    def __init__(self, color, width=100, height=100):
       super().__init__(color)
       self.width = width
       self.height = height
    def area(self):
        return self.width*self.height
    def cube(self):
        z=2
        return self.width*self.height*z

rect1 = Rectangle("blue")
print(rect1.get_color())
print("Площадь прямоугольника равно",rect1.area())
rect2 = Rectangle("red", 100, 100)
print("Обьем куба равно",rect2.get_color())
print(rect2.cube())