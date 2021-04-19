fin = 0
def numCombi(arr,n,total,i):
    global fin
    if(n<0):
        return 0
    else:
        if(total-arr[n]==0 and i==1):
            fin+=1
        numCombi(arr, n-1, total,i)
        numCombi(arr, n-1, total-arr[n],i-1)
                    
    
arr = [2,4,1,4,2]
n = len(arr)-1
total = 6
i = 2
numCombi(arr, n, total,i)
print(fin) 