t = int(input())

for q_itr in range(t):
    s = str(input())
    count = 0 
    m = 2
    for i in s:
        if (i == "A" and m == 0):
            count += 1
        elif (i == "B" and m == 1):
            count += 1
        elif(i == "A"):
            m = 0
        else:
            m = 1
            
    print(count)