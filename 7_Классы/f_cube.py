class Square:
  width = 0
  height = 0
  def __init__(self,width,hight):
    self.width=width
    self.height=height
class Cube(Square):
  z = 0
def __init__(self,width,height,z):
  Square.__init__(self,width,height)
  self.z = z
def volume(self):
  return self.area(self)*self.z
c=Cube(100,56,89)  
a = c.area()
print(" Значение a равно",a)
v = c.volume()
print(" Значение v равно",v)
