import math
class Circle():
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    @property
    def Perimetro(self):
        Perimetro = self.radius*math.pi*2
        return Perimetro
        
    @property
    def Area(self):
        Area = self.radius*math.pi**2
        return Area

r  = int(input ("Ingrese el radio: "))
color  = str(input ("Ingrese el color: "))
n =  Circle(r, color)
print("Color: "+n.color)
print("Area: "+str(n.Area))
print("Perimetro: "+str(n.Perimetro))