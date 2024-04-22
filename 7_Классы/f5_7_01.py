class Country:
 
    def __init__(self, name, population, area, coastline=0):
        self.name = name
        self.population = population
        self.area = area
        self.coastline = coastline
 
    def __repr__(self):
        return (
            f"Country(name={self.name!r}, population={self.population!r},"
            f" coastline={self.coastline!r})"
        )
 
    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (
                (self.name, self.population, self.coastline)
                == (other.name, other.population, other.coastline)
            )
        return NotImplemented
 
    def __ne__(self, other):
        if other.__class__ is self.__class__:
            return (
                (self.name, self.population, self.coastline)
                != (other.name, other.population, other.coastline)
            )
        return NotImplemented
 
    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return ((self.name, self.population, self.coastline) < (
                other.name, other.population, other.coastline
            ))
        return NotImplemented
 
    def __le__(self, other):
        if other.__class__ is self.__class__:
            return ((self.name, self.population, self.coastline) <= (
                other.name, other.population, other.coastline
            ))
        return NotImplemented
 
    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return ((self.name, self.population, self.coastline) > (
                other.name, other.population, other.coastline
            ))
        return NotImplemented
 
    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return ((self.name, self.population, self.coastline) >= (
                other.name, other.population, other.coastline
            ))
        return NotImplemented
 
    def beach_per_person(self):
        """Метры береговой линии на человека"""
        return (self.coastline * 1000) / self.population
norway = Country("Norway", 5320045, 323802, 58133)
# country1=Country(name='Norway', population=5320045, coastline=58133)
print(norway)
# norway1=norway.area
# usa = Country("United States", 326625791, 9833517, 19924)
# nepal = Country("Nepal", 29384297, 147181)
# nepal(name='Nepal', population=29384297, coastline=0)
# usa.beach_per_person()
# norway.beach_per_person()
# norway = Country("Norway", 5320045, 323802, 58133)
# norway
# Country(name='Norway', population=5320045, coastline=58133)
 
# norway.area
# 323802
 
# usa = Country("United States", 326625791, 9833517, 19924)
# nepal = Country("Nepal", 29384297, 147181)
#  nepal
# Country(name='Nepal', population=29384297, coastline=0)
 
# usa.beach_per_person()

 
# norway.beach_per_person()
