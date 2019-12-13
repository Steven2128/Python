# -*- coding: utf-8 -*-
class Gato:
   def __init__(self, nombre, color, peso, edad, vacunas):
      self.nombre = nombre
      self.color = color
      self.peso = peso
      self.edad = edad
      self.vacunas = vacunas

def run():
   gato = Gato('Loky', 'Blanco','3.5 Kg','11 meses','Si')
   print(gato.nombre)
   print('***********************')
   print('Nombre: '+gato.nombre)
   print('Color: '+gato.color)
   print('Peso: '+gato.peso)
   print('Edad: '+gato.edad)
   print('Vacunas: '+gato.vacunas)
  
if __name__ == '__main__':
   run()