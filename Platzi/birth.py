ar = [2,6,7,7,8,9,6,9,2,2,2]
mayor_num = ar[0]
cont = 0

for i in range(len(ar)):
    if ar[i]>mayor_num or ar[i]==mayor_num:
        mayor_num = ar[i]

mayor = ar.count(mayor_num)
print(mayor)