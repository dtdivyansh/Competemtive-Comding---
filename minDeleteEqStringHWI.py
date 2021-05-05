a = input()
b = input()
c = input()

l1=len(a)
l2=len(b)
l3=len(c)

m = max([l1,l2,l3])

if(l1!=m):
    a = '_'*(m-len(a))+a
    
if(l2!=m):
    b = '_'*(m-len(b))+b
    
if(l3!=m):
    c = '_'*(m-len(c))+c

cost=0
i=m-1  

while(i>=0):
    if(a[i]==b[i] and a[i]==c[i] and b[i]==c[i]):
        cost+=1
    else:
        break
    i-=1

val = l1-cost + l2-cost + l3-cost
print(val)    

        
    