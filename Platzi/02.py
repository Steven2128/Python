n = int(input())

arr = list(map(int, input().rstrip().split()))

m = int(input())

brr = list(map(int, input().rstrip().split()))
m = max(arr + brr)

table = [0 for i in range(m+1)]

for a in arr:
    table[a] += 1

for b in brr:
    table[b] -= 1

values = [y for y in range(len(table)) if table[y] != 0]
print(values)