class Rectangle:
   little="Маленький " 
   gross = "Большой" 
   color = "Зеленный"
   width = 100
   height = 100
   def square(self):
       return self.width*self.height

color_Rectangle = Rectangle()
print("Цвет первого прямоугоника",color_Rectangle.color)
ploshad_Rectangle = Rectangle()
print("Площадь первого прямоугоника",ploshad_Rectangle.square())
vtoroi_Restangle = Rectangle()
vtoroi_Restangle.width = 200
vtoroi_Restangle.gross = "Большой"
vtoroi_Restangle.little = "Маленький четерехугольник "
print("Цвет второго  прямоугоника",vtoroi_Restangle.color,vtoroi_Restangle.gross)
print("Ширина второго прямоугоника",vtoroi_Restangle.width,vtoroi_Restangle.little)
