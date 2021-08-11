def mergeLists(head1, head2):
    p = SinglyLinkedListNode(None)
    h = p
    while(head1!=None and head2!=None):
        if(head1.data>head2.data):
            p.next = SinglyLinkedListNode(None)
            p.data = head2.data
            head2 = head2.next
            p = p.next
        else:
            p.next = SinglyLinkedListNode(None)
            p.data = head1.data
            head1 = head1.next
            p = p.next
            
    while(head1!=None):
        p.data = head1.data
        head1 = head1.next
        if(head1!=None):
            p.next = SinglyLinkedListNode(None)
            p = p.next
        else:
            p.next = None
            break
        
    while(head2!=None):
        p.data = head2.data
        head2 = head2.next
        if(head2!=None):
            p.next = SinglyLinkedListNode(None)
            p = p.next
        else:
            p.next = None
            break
    
    return h
