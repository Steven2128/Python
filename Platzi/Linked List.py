
def insertNodeAtPosition(head, data, position):
    node = head
    for _ in range(position - 1):
        n = n.next
        n_next = n.next
    n.next = SinglyLinkedListNode(data)
    n.next.next = n_next
    return head

