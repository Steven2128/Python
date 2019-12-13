import math
from collections import deque
n = int(input())
li = deque()
li.append(0)

for _ in range(n):
    s = input().split()
    if s[0]=="1":
        li.append(int(s[1]))
    elif s[0]=="2":
        if li:
            li.pop()
    else:
        list_max = max(li)
        print(list_max)