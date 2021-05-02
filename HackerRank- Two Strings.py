def twoStrings(s1, s2):
    dic = {}
    for i in s1:
        dic[i]=1
    for j in s2:
        if(j in dic.keys()):
            dic[j]=2
    v = list(dic.values())
    
    if(2 in v):
        return 'YES'
    return 'NO'
