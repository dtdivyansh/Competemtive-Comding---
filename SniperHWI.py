n = int(input())

arr = [[0,0] for i in range(n)]

for i in range(n):
    arr[i][0] = int(input())  #Position
    
for i in range(n):
    arr[i][1] = int(input())  #Skills
    
arr.sort()

ans = []
i=0
while(i<n):
    j=i+1
    while(j<n):
        if( abs(arr[i][0]-arr[j][0])>arr[i][1]+arr[j][1] ):
            ans.append(arr[i])
            ans.append(arr[j])
            i=j-1
            break
        j+=1
    i+=1
print(ans)
