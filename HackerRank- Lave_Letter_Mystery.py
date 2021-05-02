def theLoveLetterMystery(s):
    i=0
    j=len(s)-1
    t=0
    while(i<j):
        t = t + abs( ord(s[i])-ord(s[j]) )
        i+=1
        j-=1
    return t
