def superReducedString(s):
    s = [i for i in s]
    flag=1
    while(flag):
        i=1
        j=0
        flag=0
        while(i<len(s)):
            if(s[i-1]==s[i]):
                s.pop(i-1)
                s.pop(i-1)
                i=j+1
                flag=1
            i+=1
        print(s)
    return ''.join(s) if s else 'Empty String'
