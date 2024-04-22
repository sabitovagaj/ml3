#Класс методы класса
class Rectangle:
   color = "green"
   width = 100
   height = 100
   def square(self):
       return self.width * self.height

#Полиморфизм
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

fig1 = Figure("green")
print(fig1.info())
rect1 = Rectangle("red", 24, 45)
print(rect1.info())


#Наследования
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

   def square(self):
       return self.width*self.height


rect1 = Rectangle("blue")
print(rect1.get_color())
print(rect1.square())
rect2 = Rectangle("red", 25, 70)
print(rect2.get_color())
print(rect2.square())

# Конструктор класса
class Rectangle:
   def __init__(self, color="green", width=100, height=100):
       self.color = color
       self.width = width
       self.height = height

   def square(self):
       return self.width * self.height


rect1 = Rectangle()
print(rect1.color)
print(rect1.square())
rect1 = Rectangle("yellow", 23, 34)
print(rect1.color)
print(rect1.square())



     