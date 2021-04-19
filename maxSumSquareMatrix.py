m = 0
li = []
def submat(arr,n):
    global m
    size = n
    while(n>0):
        i = 0
        j = n
        while(j<size+1):
            s = sum(arr[i:j])
            #print(arr[i:j],s)
            if(s>=m):
                li.append(arr[i:j])
                m = s
            i+=1
            j+=1
        v = int( n**(1/2) - 1 )
        n = v**2
        
arr = [1,100,3,21,-100,2,3,9,10]

submat(arr,9)

print(li)
    