arr = [1,-3,4,-5,-6,8,3,5]
k=3
n=len(arr)
stack=[]
res = []
i=0
j=0

while(j<n):
    if(arr[j]<0):
        stack.append(arr[j])
    if(j-i+1!=k):
        j+=1
    else:
        if(stack):
            res.append(stack[0])
            if(stack[0]==arr[i]):
                stack.pop(0)
        else:
            res.append(0)
        i+=1
        j+=1
print(res)