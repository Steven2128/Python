def hourglassSum(arr):
    li=[]
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):

          li.append(sum(arr[i][j:j+3]+arr[i+2][j:j+3])+arr[i+1][j+1])

    return max(li)