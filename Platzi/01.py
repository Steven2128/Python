arr = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470]
arr = sorted(arr)
arr_b = []
for i in range(len(arr) - 1):
    arr_b.append(arr[i+1] - arr[i])
    
value = min(arr_b)
result = []

for i in range(len(arr) - 1):
    if (arr[i+1] - arr[i]) == value:
        result.append(arr[i])
        result.append(arr[i+1])

print(result)