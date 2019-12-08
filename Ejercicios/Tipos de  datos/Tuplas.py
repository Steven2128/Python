my_tuple = (1,2,3,4,6)
#Buscar elementos en la tupla
print(my_tuple.index(2))

num = int(input("Ingrese numero a buscar: "))
if num in my_tuple:
    print("El numero "+str(num)+" SI esta en la tupla")
else:
    print("El numero "+str(num)+" NO esta en la tupla")