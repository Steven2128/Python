igual = 1
    while headA and headB:
        if headA.data != headB.data:
            igual = 0
        headA = headA.next
        headB = headB.next
    if headA or headB:
        igual = 0
    return igual