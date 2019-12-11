n = int(input())

arr = list(map(int, input().rstrip().split()))
arr.sort()
media = len(arr)//2
print(arr[media])