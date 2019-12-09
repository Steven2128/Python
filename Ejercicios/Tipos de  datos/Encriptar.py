KEYS = {
    'a' : 'w',
    'b' : 'E',
    'c' : 'x',
    'd' : '1',
    'e' : 'a',
    'f' : 't',
    'g' : '0',
    'h' : 'C',
    'i' : 'b',
    'j' : '!',
    'k' : 'z',
    'l' : '8',
    'm' : 'M',
    'n' : 'I',
    'o' : 'd',
    'p' : '.',
    'q' : 'U',
    'r' : 'Y',
    's' : 'i',
    't' : '3',
    'u' : ',',
    'v' : 'J',
    'w' : 'N',
    'x' : 'f',
    'y' : 'm',
    'z' : 'W',
    'A' : 'G',
    'B' : 'S',
    'C' : 'j',
    'D' : 'n',
    'E' : 's',
    'F' : 'Q',
    'G' : 'o',
    'H' : 'e',
    'I' : 'u',
    'J' : 'g',
    'K' : '2',
    'L' : '9',
    'M' : 'A',
    'N' : '5',
    'O' : '4',
    'P' : '?',
    'Q' : 'c',
    'R' : 'r',
    'S' : 'O',
    'T' : 'P',
    'U' : 'h',
    'V' : '6',
    'W' : 'q',
    'X' : 'H',
    'Y' : 'R',
    'Z' : 'l',
    '0' : 'k',
    '1' : '7',
    '2' : 'X',
    '3' : 'L',
    '4' : 'p',
    '5' : 'v',
    '6' : 'T',
    '7' : 'V',
    '8' : 'y',
    '9' : 'K',
    '.' : 'Z',
    ',' : 'D',
    '?' : 'F',
    '!' : 'B',
}

def encriptar(mensaje):
    words = mensaje.split(' ')
    encriptar_mensaje = []

    for word in words:
        encriptar_palabra = ''

        for letter in word:
            encriptar_palabra += KEYS[letter]
            
        encriptar_mensaje.append(encriptar_palabra)
    return' '.join(encriptar_mensaje)


def desencriptar(mensaje):
    words = mensaje.split(' ')
    desencriptar_mensaje = []

    for word in words:
        desencriptar_palabra = ''

        for letter in word:

            for key, valor in KEYS.items():

                if valor == letter:
                    desencriptar_palabra += key

        desencriptar_mensaje.append(desencriptar_palabra)
    return' '.join(desencriptar_mensaje)


def run():

    while True:

        menu = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [a] Cifrar un mensaje
            [b] Decifrar un mensaje
            [s] Salir del programa
        '''))

        if menu == 'a'or menu =='A':
            mensaje = str(input('ESCRIBE TU MENSAJE: '))
            encriptar_mensaje = encriptar(mensaje)
            print(encriptar_mensaje)

        elif menu == 'b'or menu == 'B':
            mensaje = str(input('ESCRIBE TU MENSAJE CIFRADO: '))
            desencriptar_mensaje = desencriptar(mensaje)
            print(desencriptar_mensaje)

        elif menu == 's'or menu == 'S':
            exit()

        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()