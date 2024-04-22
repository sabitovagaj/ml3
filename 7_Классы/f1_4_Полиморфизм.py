class Figure:
   def __init__(self, color):
       self.color = color
      
   def get_color(self):
       return self.color
      
   def info(self):
       print("Figure")
       print("Color: " + self.color)


class Rectangle(Figure):
   def __init__(self, color, width=100, height=100):
       super().__init__(color)
       self.width = width
       self.height = height

   def square(self):
       return self.width * self.height

   def info(self):
       print("Rectangle")
       print("Color: " + self.color)
       print("Width: " + str(self.width))
       print("Height: " + str(self.height))
       print("Square: " + str(self.square()))
       print("На этом все: ")

fig1 = Figure("Зеленный")
print(fig1.info())
rect1 = Rectangle("Красный", 24, 45)
print(rect1.info())
