arr = [5,4,2,3,1,1,3,5]

k = 5

win = 0

i=0
j=0

s=0
while(j<len(arr)):
    s+=arr[j]
    
    if(s<k):
        j+=1
    elif(s==k):
        win = max(win,j-i+1)
        j+=1
    else:
        while(s>k):
            s = s - arr[i]
            i+=1
        if(s<k):
            j+=1
        else:
            win = max(win,j-i+1)
            j+=1

print(win)
        
