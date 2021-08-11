def removeDuplicates(llist):
    h = llist
    while(h!=None and h.next!=None):
        p = h
        h = h.next
        while(p.data == h.data):
            h = h.next
            if(h==None):
                break
                
        p.next = h    
        
    return llist
