n = int(input())

arr = [0]*(n+1)

for i in range(2,n+1):
    if(arr[i]==0):
        for j in range(i*i,n+1,i):
            arr[j] = 1
c=0            
for i in range(2,n+1):
    if(arr[i]==0):
        c+=1
        #print(i)
print(c)        


