#-*- coding: utf-8 -*-
def main(word):
    reverse_word = word[::-1]
    if reverse_word==word:
        return True
    else:
        return False
    


if __name__ == "__main__":
    word = input("Ingrese una palabra: ")
    Result = main(word)
    if Result==True:
        print(word+" sí es un palíndromo")
    else:
        print(word+" no es un palíndromo")