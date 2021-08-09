def insertNodeAtPosition(llist, data, position):
    node = SinglyLinkedListNode(data)
    if(position==0):
        node.next = llist
        llist = node
        return llist
    else:
        p = llist
        for i in range(position-1):
            p = p.next
        v = p.next
        p.next = node
        node.next = v
        return llist
