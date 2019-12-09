class Vector():
    def __init__(self, i , j, k):
        self.i  = float(i)
        self.j  = float(j)
        self.k  = float(k)
        

    def __add__(self, v):
        suma_i = self.i + v.i
        suma_j = self.j + v.j
        suma_k = self.k + v.k
        vector_suma = Vector(suma_i, suma_j, suma_k)
        return vector_suma

    def __sub__(self, v):
        resta_i = self.i - v.i
        resta_j = self.j - v.j
        resta_k = self.k - v.k
        vector_resta = Vector(resta_i, resta_j, resta_k)
        return vector_resta
    
    def __mul__(self, v):
        multi_i = self.i * v.i
        multi_j = self.j * v.j
        multi_k = self.k * v.k
        vector_multi = Vector(multi_i, multi_j, multi_k)
        return vector_multi

    
v1 = Vector(1, 1, 1)
v2 = Vector (5, -3, 4)
vector_suma  = v1 + v2
vector_resta = v1 - v2
vector_multi = v1 * v2
print("La magnitud  del ")
suma  = []
resta = []
multi = []
suma.append(vector_suma.i)
suma.append(vector_suma.j)
suma.append(vector_suma.k)
print("Suma de los vectores: "+str(suma))
resta.append(vector_resta.i)
resta.append(vector_resta.j)
resta.append(vector_resta.k)
print("Resta de los vectores: "+str(resta))
multi.append(vector_multi.i)
multi.append(vector_multi.j)
multi.append(vector_multi.k)
print("La multiplicación de los vectores: "+str(multi))
