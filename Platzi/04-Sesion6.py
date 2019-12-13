from collections import deque


def transfer_elements(del_s, ins_s):
    while len(ins_s) > 0:
        del_s.append(ins_s.pop())

N = int(input())
insert_s = deque()
delete_s = deque()
for _ in range(N):
    q = [int(x) for x in input().split()]
    if q[0] == 1:
        x = q[1]
        insert_s.append(x)
    elif q[0] == 2:
        if len(delete_s) == 0:
            transfer_elements(delete_s, insert_s)
        delete_s.pop()
    else:
        if len(delete_s) == 0:
            transfer_elements(delete_s, insert_s)
        print(delete_s[-1])