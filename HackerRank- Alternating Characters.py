def alternatingCharacters(s):
    dic = {'A':[] , 'B':[]}
    for i in range(len(s)):
        dic[s[i]].append(i)
    A = dic['A']
    B = dic['B']
    t=0
    for i in range(1,len(A)):
        if(A[i]-A[i-1]==1):
            t+=1
    
    for i in range(1,len(B)):
        if(B[i]-B[i-1]==1):
            t+=1
            
    return t
