# -*- coding: utf-8 -*-

import random

#seleccion automatica de la palabra
palabras_posibles = ['leon','tigre','murcielago','peyorativo','misantropia',
                    'hipotalamo','ventriculo','esclerosis','necrosis','isquemia',
                    'filantropia','epilepsia']
palabra_seleccionada = palabras_posibles[random.randint(0,len(palabras_posibles)-1)]

#Figuras a dibujar
IMAGES = ['''   

    +---+
    |   |
        |
        |
        |
        |
        =========''','''   

    +---+
    |   |
    0   |
        |
        |
        |
        =========''','''   

    +---+
    |   |
    0   |
    |   |
        |
        |
        =========''','''   

    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''','''   

    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''','''   

    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''','''   

    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''','''   

    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''']

FIN_DIBUJO = ['''--- * --- * --- * --- * --- * --- * --- * --- * --- * ---''']

#parametros
x = 0#x es la cantidad de fracasos
y = len(palabra_seleccionada) # es la cantidad de letras de la palabra que se selecciona al azar

#construyo una palabra sustituta para irla completando de a poco
string = '-'
largo = string*y
palabra_sustituta = list(largo)

def dibujo_inicial(x):
    print(IMAGES[x])
    print('')
    print(palabra_sustituta)
    print('')
    print(FIN_DIBUJO[0])
    print('')


def intento(x):#esta funcion va a incorporar todas las variables
    letra_seleccionada = (str(input('Escoge una letra: ')))
    a = y #uso 'a' para ir contando las derrotas

    for i in range(y):
        if letra_seleccionada == palabra_seleccionada[i]:
            palabra_sustituta[i] = letra_seleccionada
        else:
            a -= 1
    if a == 0:
        x += 1
        dibujo_inicial(x)
        if x >= (len(IMAGES)-1):
            print('Perdiste, la palabra es: '+str(palabra_seleccionada))
            print(' ')
        else:
            intento(x)
    else:
        if palabra_sustituta == list(palabra_seleccionada):
            dibujo_inicial(x) 
            print('felicitaciones, ganaste!')
            pass
        else:
            dibujo_inicial(x)   
            intento(x)
        pass


if __name__ == '__main__':
    dibujo_inicial(0)
    intento(x)