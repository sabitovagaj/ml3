class Square:
    width=0
    height=0
    def area(self):
        return self.width*self.height
class Cube:
    z=0
    def __init__(self,width,height,z):
        Square.__init__(self,width,height)
        self.z=z
    def volume(self):
        return area(self)*self.z
c = Cube(100,40,5)
a=c.area()
v=c.volume()
print("Площадь прямоугоника равна sq=",a)
print("Площадь прямоугоника равна sq=",v) 