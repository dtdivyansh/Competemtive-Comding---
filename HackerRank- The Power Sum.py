def sol(x,n,r,d):
    if((d>r and x!=0) or x<0):
        return 0
    elif(x==0):
        return 1
    else:
        a = sol(x - d**n,n,r,d+1)
        b = sol(x,n,r,d+1)
        return a+b

def powerSum(X, N):
    r = int(X**(1/2))+1
    count = sol(X,N,r,1)
    return count
