def anagram(s):
    n=len(s)
    if(n%2!=0):
        return -1
    t = s[:n//2]
    s = s[n//2:]
    count = 0
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    dic1 = {}
    dic2 = {}
    for val in alpha:
        dic2[val] = t.count(val)
        dic1[val] = s.count(val)
            
    for i in dic2:
        c1 = dic2[i]
        c2 = dic1[i]
        if(c1>c2):
            count+=(c1-c2)
                
    return count
