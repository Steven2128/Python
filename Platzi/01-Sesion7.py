t = int(input())

for t_itr in range(t):
    n = int(input())
    new_n = str(n)
    suma=0
    for i in range(len(new_n)):
        if int(new_n[i])==0:
            suma+=0
        elif n%int(new_n[i])==0:
            suma+=1
    print(suma)
    
        


    