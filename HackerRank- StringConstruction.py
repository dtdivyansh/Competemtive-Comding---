def stringConstruction(s):
    cost=1
    for i in range(1,len(s)):
        if( s[i] not in s[0:i] ):
            cost+=1
    return cost
