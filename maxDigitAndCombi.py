def max3(arr):
    dic = {}
    res = ''
    for i in sorted(arr,reverse=True):
        res+=str(i)
        if(len(res)==3):
            break
    n = int(res)
    
    l = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if(i==j or i == k or j == k):
                    pass
                else:
                    t = [arr[i],arr[j],arr[k]]
                    if(t not in l):
                        l.append(t)
                        
    
    c = len(l)
    print(n,c)
 
arr = [int(i) for i in input().split()]

max3(arr)    
