def gemstones(arr):
    dic = {}
    for i in 'abcdefghijklmnopqrstuvwxyz':
        dic[i]=0
    for s in arr:
        s = list(map(str,s))
        s = set(s)
        s = list(s)
        for i in s:
            dic[i]+=1
    n = len(arr)
    t = 0
    for key in dic.keys():
        if(dic[key]==n):
            t+=1
    return t
