def gameOfThrones(s):
    dic = {}
    for i in s:
        if(i in dic.keys()):
            dic[i]+=1
        else:
            dic[i]=1
    t=0
    for n in dic.values():
        if(n%2!=0):
            t+=1
    if(t>1):
        return 'NO'
    else:
        return 'YES'
