arr = [3,3,1,-1,-2,-5,0,4]

m = [0]

k = 3
v = []
i=0
j=0

while(j<len(arr)):
    if(arr[j]>=arr[m[0]]):
        m=[j]
    else:
        m.append(j)
    if(j-i+1!=k):
        j+=1
    else:
        v.append(arr[m[0]])
        if(i==m[0]):
            m.pop(0)
        i+=1
        j+=1
        
print(v)
 