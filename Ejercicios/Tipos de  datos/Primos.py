# -*- coding: utf-8 -*-
def primo(number):
    if  number < 2:
        return False
    elif number==2:
        return True
    elif number > 2 and number%2 == 0:
        return False
    else:
        for i in range(3,number):
            if number % i == 0:
                return  False
    return  True
def run():
    number = int(input("Ingresa un número: "))
    result = primo(number)

    if result==True:
        print("Primo!")
    else:
        print("No primo")

if __name__ == "__main__":
    run()