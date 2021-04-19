def permutation(s,i,n,pos,char):
    global res
    if(i==n and s[pos]!=char):
        res.append( ''.join(s) )
    else:
        for j in range(i,n):
            swap(s,i,j)
            permutation(s, i+1, n,pos,char)
            swap(s,i,j)
        


def swap(s,i,j):
    s[i],s[j] = s[j],s[i]


s = input()
s = [i for i in s]
res = []
permutation(s, 0, len(s),1,'b')

res.sort()

print(res)
