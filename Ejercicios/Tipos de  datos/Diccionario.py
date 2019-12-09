mi_diccionario = {"Key": "Value", "Hola": "Mundo"}

print("Iterar en llaves")
for key in mi_diccionario.keys():
    print(key)

print("")
print("Iterar en valores")
for value in mi_diccionario.values():
    print(value)

print("")
print("Iterar en items")
for key, value in mi_diccionario.items():
    print(key+":"+ value)

print("")
key = str(input("Ingrese la llave: ")).capitalize()
print(mi_diccionario.get(key))