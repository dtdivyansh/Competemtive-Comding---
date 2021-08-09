def reverse(llist):
    p = None
    v = llist
    while(v!=None):
        k = v.next 
        v.next = p
        p = v
        if(k==None):
            break
        v = k
     
    return v
