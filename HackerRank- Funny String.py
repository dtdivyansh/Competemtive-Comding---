def funnyString(s):
    n1 = ord(s[0])
    n2 = ord(s[-1])
    n = len(s)
    for i in range(1,n):
        v1 = abs(n1-ord(s[i]))
        v2 = abs(n2-ord(s[n-i-1]))
        if(v1!=v2):
            return 'Not Funny'
        else:
            n1 = ord(s[i])
            n2 = ord(s[n-i-1])
    return 'Funny'
