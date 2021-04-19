t = int(input())
while(t>0):
    n = int(input())
    st = input().split()
    s1 = st[0]
    s2 = st[1]
    c = 0
    
    dic1 = {}
    dic2 = {}
    
    for s in s1:
        if( s not in dic1.keys() ):
            dic1[s] = 1
        else:
            dic1[s]+=1
            
    for s in s2:
        if( s not in dic2.keys()):
            dic2[s] = 1
        else:
            dic2[s]+=1
            
    for i in dic1.keys():
        if( i in dic2.keys()):
            val1 = dic1[i]
            val2 = dic2[i]
            if(val1 > val2):
                dic1[i]-=val2
                dic2[i] = 0
            elif(val1<val2):
                dic1[i]=0
                dic2[i]-=val1
            else:
                dic1[i]=0
                dic2[i]=0
            
    res = sum(dic1.values()) + sum(dic2.values())
    print(res//2)
    t-=1
