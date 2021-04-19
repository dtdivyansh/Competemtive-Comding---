def nearest_palindrome(n):
    c=0
    arr = [ int(i) for i in str(n) ]
    i = 0
    j = len(arr)-1
    while(i<=j):
        if(arr[i]>arr[j]):
            arr[j] = arr[i]
        elif(arr[i]==arr[j]):
            if(i==j and c!=0):
                arr[i]+=1
                c = 0
            elif(j-i==1 and c!=0):
                arr[i]+=1
                arr[j]+=1
                c=0
        else:
            arr[j] = arr[i]
            if(c!=0):
                arr[i]+=1
                arr[j]+=1
                c=0
            else:
                c=1
        i+=1
        j-=1
    print(arr)
    
n = int(input())
 
k=nearest_palindrome(n)
print(k)