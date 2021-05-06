num = [int(i) for i in input()]

per = 1
zero=0
low=1
high=0
prev=1
for i in range(len(num)):
    if(num[i]==0):
        zero+=1
    elif(num[i]!=0 and not zero):
        low=num[i]
    elif(num[i]!=0 and zero):
        high=num[i]
        val = high-low+1
        if(zero==1):
            per = per*val
            zero=0
        else:
            s = val*(val+1)//2
            c = zero-1
            per = per*c*s
            zero=0
        low=num[i]
if(zero):
    high=9
    val = high-low+1
    if(zero==1):
        per = per*val
    else:
        s = val*(val+1)//2
        c = zero-1
        per = per*c*s
        
print(per%(10**9 + 7))
    