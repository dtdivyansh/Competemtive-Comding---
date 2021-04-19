def three(arr,n):
    if(n<3):
        return -1
    else:
        mi = 1000
        for i in range(n-2):
            for j in range(n-2):
                t = arr[i][j]
                if(t==arr[i+1][j+1] and t==arr[i+2][j+2]):
                    if(mi>t):
                        mi=t
                elif(t==arr[i+1][j] and t==arr[i+2][j]):
                    if(mi>t):
                        mi=t
                elif(t==arr[i][j+1] and t==arr[i][j+2]):
                    if(mi>t):
                        mi=t
                    
            for j in range(n-1,2,-1):
                t = arr[i][j]
                if(t==arr[i+1][j-1] and t==arr[i+2][j-2]):
                    if(mi>t):
                        mi=t
                elif(t==arr[i][j-1] and t==arr[i][j-2]):
                    if(mi>t):
                        mi=t
                elif(t==arr[i+1][j] and t==arr[i+2][j]):
                    if(mi>t):
                        mi=t
        
        return mi

arr = [ [7,2,3,4],[2,7,9,2],[2,1,7,4],[4,2,1,3] ]      
n= len(arr)

val = three(arr,n)

print(val)  
                