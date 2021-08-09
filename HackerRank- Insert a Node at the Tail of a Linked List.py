def insertNodeAtTail(head, data):
    p = head
    if(head==None):
        head = SinglyLinkedListNode(data)
        return head
    
    while(p.next!=None):
        #print(p.data)
        p = p.next
        
        
    n = SinglyLinkedListNode(data)
    p.next = n
    
    return head
