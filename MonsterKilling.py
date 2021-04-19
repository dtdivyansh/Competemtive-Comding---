n = int(input())
exp = int(input()) 

power = [int(i) for i in input().split()]

bonus = [int(i) for i in input().split()]

c = 0

while(True):
    flag = 0
    l = len(power)
    for i in range(l):
        if( exp>=power[i] and power[i] ):
            power[i]=0
            c+=1
            exp+=bonus[i]
            flag = 1
    if(flag==0):
        break
    
print(c)
            
        