
#por convension el nombre de las clases inician con mayusculas utilizando CamelCase
class Lamp:
    #por convension la declaracion de variables o metodos privados se definen con _ antes del nombre
    _LAMPS = ['''
            |   
         \ .-. /        
       -- (   ) --
           \ /
          _|=|_
         |_____|  
    ''','''

           .-. 
          (   )
           \ /
          _|=|_
         |_____|  
    ''']
    #todos los metodos en las clases deben de recibir el objeto self
    #el metodo __init__ es el constructor
    def __init__(self, isTurnedOn):
        self.isTurnedOn = isTurnedOn

    def turnOn(self):
        self.isTurnedOn = True
        self._displayImage()

    def tunrOff(self):
        self.isTurnedOn = False
        self._displayImage()

    def _displayImage(self):
        if self.isTurnedOn:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

def run():
    lamp = Lamp(isTurnedOn=False)
    while True:
        command = str(input('''
        Que deseas hacer?
        [p]render
        [a]pagar
        [s]alir
        ''')).lower()

        if command=='p':
            lamp.turnOn()
        elif command == 'a':
            lamp.tunrOff()
        elif command == 's':
            break
        else:
            print('opcion no valida')

if __name__ == '__main__':
    run()