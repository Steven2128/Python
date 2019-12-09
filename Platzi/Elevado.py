num = int(input("Ingrese  un  número: "))
if num  < 0:
    num = num*(-1)
exp = int(input("Ingrese  el exponente: "))

for i in range(num+1):
    r = i**exp
    print(str(i)+" elevado a la "+str(exp)+" es: "+str(r))
    