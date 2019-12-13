def suma_Recur(num):
    cont = [num]
    num = int(input("Ingresa el número a sumar: "))
    cont[0] = cont[0]+num
    print("La suma es: "+str(cont[0]))
    suma_Recur(cont[0])
    
def run():
    num = int(input("Ingresa el número a sumar: "))
    suma_Recur(num)

if __name__ == "__main__":
    run()