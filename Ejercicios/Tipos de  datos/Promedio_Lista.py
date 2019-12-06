#-*- coding: utf-8 -*-
def main():
    suma = 0
    temps = [20,32,21,25,40,26]
    for i in temps:
        suma +=float(i)

    return suma/len(temps)

if __name__ == "__main__":
    Result = main()
    print("El promedio de las temperaturas es: "+str(Result))