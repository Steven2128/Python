from collections import deque

stack = deque()
stack.append(0)

N = int(input())
for i in range(N):
    inst = input()
    if inst[0] == '1':
        x = int(inst.split()[-1])
        stack.append(max(x, stack[-1]))
    elif inst[0] == '2':
        stack.pop()
    else:
        print(stack[-1])