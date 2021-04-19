def find(arr,n):
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    dp2 = [[0 for i in range(n+1)] for j in range(n+1)]
    dp3 = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if(i==0 and j==0):
                dp[i][j]=0
                dp2[i][j]=0
                dp3[i][j]=0
            elif(i<n and j<n):
                if( arr[i][j] == arr[i-1][j-1] ):
                    dp[i][j]=1+dp[i-1][j-1]
                if( arr[i][j] == arr[i][j-1] ):
                    dp2[i][j]=1+dp2[i][j-1]
                if( arr[i][j] == arr[i-1][j] ):
                    dp3[i][j]=1+dp3[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1]
                dp2[i][j] = dp2[i][j-1]
                dp3[i][j] = dp3[i-1][j]
                
                
    c=1000007
    for i in range(n+1):
        for j in range(n+1):
            if( dp[i][j]>=3 and arr[i-1][j-1]< c ):
                c = arr[i-1][j-1]
            elif( dp2[i][j]>=3 and arr[i][j-1]< c ):
                c = arr[i][j-1]
            elif( dp3[i][j]>=3 and arr[i-1][j]< c ):
                c = arr[i-1][j]
                
    if(c==1000007):
        return -1
    return c
                

n = int(input())

arr= []

for j in range(n):
    temp = [int(i) for i in input().split()]
    arr.append(temp)
    
val = find(arr,n)
print(val)
    