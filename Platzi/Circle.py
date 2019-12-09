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
        
n =  Circle(3,"Blanco")
print("Area: "+str(n.Area()))
print("Perimetro: "+str(n.Perimetro()))