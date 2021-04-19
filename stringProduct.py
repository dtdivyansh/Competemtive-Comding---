def existProd(s,n):
    arr = [int(i) for i in s]
    l = []
    for i in range(n-1):
        j = i+1
        if(arr[j]-arr[i]==1):
            mul = arr[j]*arr[i]
            if(str(mul) in s):
                l.append(str(mul))
    if(l):
        print(l)
    else:
        print(-1)
        
s = '1203456'
existProd(s, len(s)) 
                    