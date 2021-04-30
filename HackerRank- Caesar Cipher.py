def caesarCipher(s, k):
    s = list(map(str,s))
    a = list(map(str,'abcdefghijklmnopqrstuvwxyz'))
    A = list(map(str,'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    for i in range(len(s)):
        if(s[i].isupper()):
            v = (A.index(s[i])+k)%26
            s[i] = A[v]
        elif(s[i].islower()):
            v = (a.index(s[i])+k)%26
            s[i] = a[v]
    return ''.join(s)
