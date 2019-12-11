def rotar(a, r):
    l = a[r:] + a[:r]
    return l
nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))
r = d % n

print(*rotar(a,r))