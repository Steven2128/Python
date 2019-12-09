import math
class Circle():
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def Perimetro(self):
        Parametro = self.radius*math.pi*2
        return Parametro

    def Area(self):
        Area = self.radius*math.pi**2
        return Area
r  = int(input ("Ingrese el radio: "))
color  = str(input ("Ingrese el color: "))
n =  Circle(r, color)
print("Area: "+str( n.Area()))
print("Perimetro: "+str(n.Perimetro()))