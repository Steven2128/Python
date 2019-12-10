n = int(input())
numeros =  []
l = [-1, -2]
suma_iz = 0
suma_der = 0
j=0
h=-1
for i in range(n):
    li = list(input())
    numeros.append(li)
    
    suma_iz  = suma_iz+int(li[j])
    suma_der = suma_der+int(li[h])
    h-=2    
    j+=2
result = suma_iz  - suma_der
print(l[0]+ l[1])
        