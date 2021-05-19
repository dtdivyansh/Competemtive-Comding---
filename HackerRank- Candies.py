def candies(n, arr):
    cost=[1]
    j=1
    while(j<len(arr)):
        if(arr[j]>arr[j-1]):
            cost.append(cost[j-1]+1)
        else:
            cost.append(1)
        j+=1
    j=n-2
    while(j>=0):
        if(arr[j]>arr[j+1]):
            cost[j]=max(cost[j],cost[j+1]+1)
        j-=1
    print(cost)     
    return sum(cost)
