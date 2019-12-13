N = int(input())
pasos = input().strip()

valle = 0
alti = 0

for paso in steps:
    if paso == "U":
        alti += 1
        if alti == 0:
            valle += 1
    else:
        alti -= 1
print(valle)